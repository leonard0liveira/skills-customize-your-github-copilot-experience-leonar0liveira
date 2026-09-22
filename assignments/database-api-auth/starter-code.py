from fastapi import FastAPI, HTTPException, Header, status
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Task API", description="A small API with SQLite and basic authentication")

DB_NAME = "tasks.db"


class UserCreate(BaseModel):
    username: str
    password: str


class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


@app.get("/")
def read_root():
    return {"message": "Task API is running"}


@app.post("/register")
def register_user(user: UserCreate):
    conn = get_db_connection()
    try:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password),
        )
        conn.commit()
        return {"message": "User registered successfully"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Username already exists")
    finally:
        conn.close()


@app.post("/login")
def login_user(user: UserCreate):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT id, username FROM users WHERE username = ? AND password = ?",
        (user.username, user.password),
    ).fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": "Login successful", "token": f"token-{row['username']}"}


@app.get("/tasks")
def get_tasks(token: str | None = Header(default=None)):
    if token is None or "token-" not in token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, token: str | None = Header(default=None)):
    if token is None or "token-" not in token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
        (task.title, task.description, int(task.completed)),
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return {"id": task_id, "title": task.title, "description": task.description, "completed": task.completed}
