from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional

app = FastAPI()  

# Simulated database for demonstration  
database_usernames = set()  # This set will store usernames to simulate a user database.  
database_items = {}  # This dictionary will simulate an item database by item_id.  


class Address(BaseModel):  
    street: str  
    city: str  
    postal_code: str  
    state: str  
    country: str  
    zip_code: str  


class User(BaseModel):  
    id: int  
    username: str  
    name: str = Field(..., example="John Doe", min_length=2, max_length=50)  
    age: int = Field(ge=18, le=100, description="Age must be between 18 and 100.")  
    email: EmailStr = Field(description="Email address of the user.")  
    bio: Optional[str] = Field(None, max_length=300, description="A brief biography of the user.")  
    address: Address  # Nested model  

    @validator('name')  
    def name_must_contain_space(cls, v):  
        if ' ' not in v:  
            raise ValueError('Name must contain a space')  
        return v.title()  

    @validator('age')  
    def validate_age(cls, v):  
        if v < 18:  
            raise ValueError('User must be at least 18 years old')  
        return v  


class Item(BaseModel):  
    id: int  
    name: str  
    description: Optional[str] = None  
    price: float  


@app.post("/users/", response_model=User)  
async def create_user(user: User):  
    if user.username in database_usernames:  
        raise HTTPException(status_code=400, detail="Username already registered")  
    database_usernames.add(user.username)  # Add username to the simulated database  
    return user  


@app.get("/items/{item_id}", response_model=Item)  
async def read_item(item_id: int):  
    if item_id not in database_items:  
        raise HTTPException(status_code=404, detail="Item not found")  
    return database_items[item_id]
