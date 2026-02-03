from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

# --- 1. Database Setup ---
# SQLModel combines Pydantic validation with Database tables [1]
class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    quantity: int = 0
    description: str | None = None

# This creates a file named 'database.db' in your project folder
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# check_same_thread=False is needed only for SQLite
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# --- 2. Dependency Injection ---
# This helper function manages the database session for each request [2]
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

# Create the database tables when the app starts
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- 3. CRUD Endpoints ---

# CREATE
@app.post("/items/", response_model=Item)
def create_item(item: Item, session: SessionDep):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

# READ (All)
@app.get("/items/", response_model=list[Item])
def read_items(session: SessionDep):
    items = session.exec(select(Item)).all()
    return items

# READ (Single)
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, session: SessionDep):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# UPDATE
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_data: Item, session: SessionDep):
    item_db = session.get(Item, item_id)
    if not item_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Update the fields
    item_db.name = item_data.name
    item_db.price = item_data.price
    item_db.quantity = item_data.quantity
    item_db.description = item_data.description
    
    session.add(item_db)
    session.commit()
    session.refresh(item_db)
    return item_db

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int, session: SessionDep):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return {"message": "Item deleted"}