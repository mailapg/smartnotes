from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from datetime import datetime, timezone

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["smart_notes"]
collection = db["notes"]

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def index(request: Request):
    notes = list(collection.find())
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})
    
@app.post("/create")
def create_note(title: str = Form(...), content: str = Form(...), tags: str = Form("")):
    note = {
        "title": title,
        "content": content,
        "tags": [tag.strip() for tag in tags.split(",") if tag.strip()],
        "created_at": datetime.now(timezone.utc)
    }
    collection.insert_one(note)
    return RedirectResponse(url="/", status_code=303)

