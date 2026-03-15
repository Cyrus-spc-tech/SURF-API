from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
# for html frontend
from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="template")


class Item(BaseModel):
    name: str
    price: float
    quantity: int = 0
    description: Optional[str] = None


items_db:Dict[int,Item]={}

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("mainhm.html",{"request":request})


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




# update 

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    # Update the item in the dictionary
    items_db[item_id] = item
    return {"message": "Item updated", "item": item}



# delete 

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted"}

