from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from pathlib import Path

from routers.notes import get_notes_router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["smart_notes"]
collection = db["notes"]

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

app.include_router(get_notes_router(collection))