from fastapi import FastAPI, status
from typing import Optional


app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Welcome to our API!"}




@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # FastAPI automatically validates and converts
    return {"user_id": user_id}



# path parameters to search specific 
@app.get("/items/{category_id}/products/{product_id}")
async def get_product(category_id: int, product_id: int):
    return {"category_id": category_id, "product_id": product_id}



# uses query parameters to filter data
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10, search: Optional[str] = None):
    items = fetch_items(skip=skip, limit=limit, search_query=search)
    return {"items": items, "skip": skip, "limit": limit}