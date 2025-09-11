from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pymongo.collection import Collection
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

def get_notes_router(collection: Collection):
    router = APIRouter()

    @router.get("/")
    def index(request: Request):
        notes = list(collection.find())
        return templates.TemplateResponse("index.html", {"request": request, "notes": notes})

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