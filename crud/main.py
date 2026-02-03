from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: int = 0
    description: Optional[str] = None


items_db:Dict[int,Item]={}


#create
@app.post("/item/{item_id}")
def create_item(item_id: int , item : Item):
    if item_id in items_db:
        raise HTTPException(status_code=400,detail="item already exists ")
        items_db[item_id]=item

        return{ " msg " : "Item Created", "item": item}


#read 
@app.get("/items/{item_id}")
def read_item(item_id : int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


# read all

@app.get("/items/")
def read_all():
    return items_db


