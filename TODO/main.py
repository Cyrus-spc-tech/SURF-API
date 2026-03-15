from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.database import Base, engine, SessionLocal
from routes.todo import router
from models.model import Todo

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router, prefix="/todos", tags=["Todos"])

# Configure templates
templates = Jinja2Templates(directory="template")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Enhanced FastAPI Todo App!"}

@app.get("/")
def dashboard(request: Request, db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return templates.TemplateResponse("dashboard.html", {
        "request": request, 
        "todos": todos
    })