from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pymongo.collection import Collection
from datetime import datetime, timezone
from pathlib import Path
import random

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

def get_notes_router(collection: Collection):
    router = APIRouter()

    @router.get("/")
    def index(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})
    
    @router.get("/list")
    def list_notes(request: Request):
        notes = list(collection.find().sort("created_at", -1))
        return templates.TemplateResponse("list.html", {"request": request, "notes": notes})
    
    @router.get("/create")
    def create_form(request: Request):
        return templates.TemplateResponse("create.html", {"request": request})
    
    @router.get("/random")
    def random_card(request: Request):
        notes = list(collection.find())
        note = random.choice(notes) if notes else None
        return templates.TemplateResponse("random.html", {"request": request, "note": note})

    @router.post("/create")
    def create_note(title: str = Form(...), content: str = Form(...), tags: str = Form("")):
        note = {
            "title": title,
            "content": content,
            "tags": [tag.strip() for tag in tags.split(",") if tag.strip()],
            "created_at": datetime.now(timezone.utc)
        }
        collection.insert_one(note)
        return RedirectResponse(url="/", status_code=303)

    return router