from fastapi import APIRouter, Request, Form, HTTPException, Query
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pymongo.collection import Collection
from datetime import datetime, timezone, timedelta
from pathlib import Path
from bson import ObjectId
import random
from typing import Optional
 
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")
 
OFFSET = timedelta(hours=2)
 
def _fmt(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    local_time = dt + OFFSET
    return local_time.strftime("%d.%m.%Y %H:%M")
 
 
def get_notes_router(collection: Collection):
    router = APIRouter()
 
    @router.get("/")
    def index(request: Request):
        return templates.TemplateResponse("home.html", {"request": request})
    
    @router.get("/list")
    def list_notes(request: Request, tags: Optional[str] = Query(None)):
        query = {}
        active_tags = []
        if tags:
            active_tags = [tag.strip() for tag in tags.split(",") if tag.strip()]
            if active_tags:
                query = {"tags": {"$all": active_tags}}
        notes = list(collection.find(query).sort("created_at", -1))
        for note in notes:
            note["created_at"] = _fmt(note["created_at"])
        all_tags = collection.distinct("tags")
        return templates.TemplateResponse(
            "list.html",
            {
                "request": request,
                "notes": notes,
                "all_tags": all_tags,
                "active_tags": active_tags,
            },
        )
    @router.get("/create")
    def create_form(request: Request):
        return templates.TemplateResponse("create.html", {"request": request})
    
    @router.get("/random")
    def random_card(request: Request):
        notes = list(collection.find())
        note = random.choice(notes) if notes else None
        if note:
            note["created_at"] = _fmt(note["created_at"])
        return templates.TemplateResponse("random.html", {"request": request, "note": note})
    
    @router.get("/edit/{note_id}")
    def edit_form(note_id: str, request: Request):
        note = collection.find_one({"_id": ObjectId(note_id)})
        if not note:
            raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
        note["created_at"] = _fmt(note["created_at"])
        return templates.TemplateResponse("edit.html", {"request": request, "note": note})
    
    @router.post("/create")
    def create_note(
        title: str = Form(...),
        content: str = Form(...),
        tags: str = Form("")
    ):
        note = {
            "title": title,
            "content": content,
            "tags": [tag.strip() for tag in tags.split(",") if tag.strip()],
            "created_at": datetime.now(timezone.utc)
        }
        collection.insert_one(note)
        return RedirectResponse(url="/list", status_code=303)
    
    @router.post("/edit/{note_id}")
    def update_note(
        note_id: str,
        title: str = Form(...),
        content: str = Form(...),
        tags: str = Form("")
    ):
        updated = collection.update_one(
            {"_id": ObjectId(note_id)},
            {"$set": {
                "title": title,
                "content": content,
                "tags": [tag.strip() for tag in tags.split(",") if tag.strip()]
            }}
        )
        if updated.matched_count == 0:
            raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
        return RedirectResponse(url="/list", status_code=303)
    @router.delete("/delete/{note_id}")
    def delete_note(note_id: str):
        deleted = collection.delete_one({"_id": ObjectId(note_id)})
        if deleted.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
        return RedirectResponse(url="/list", status_code=303)
    return router