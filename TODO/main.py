from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from database.database import Base, engine
from routes.todo import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router, prefix="/todos", tags=["Todos"])

# Configure templates
templates = Jinja2Templates(directory="template")


# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Enhanced FastAPI Todo App!"}


@app.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})