from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = Path(__file__).parent / "klimesnicek.db"

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/recipes")
def get_recipes():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM recipes")
    recipes = [dict(row) for row in cur.fetchall()]
    conn.close()
    return recipes

@app.get("/meal_plan")
def get_meal_plan():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM meal_plan")
    plan = [dict(row) for row in cur.fetchall()]
    conn.close()
    return plan