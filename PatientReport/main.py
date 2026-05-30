



from fastapi import FastAPI , Path , HTTPException , Query
import json

from pydantic import BaseModel ,Field, field_validator # EmailStr  >> email : EmailStr   # AnyUrl   
from typing import List,Dict,Optional



app = FastAPI()

class Address(BaseModel):
    state:str
    city:str
    pin:str

class Patient(BaseModel):
    name: str
    age : int
    marrid: Optional[bool] = None
    address: Address
    email : str


    # @field_validator('email')
    # @classmethod
    # def email_verify(cls,val):
    #     va=['gmail.com','hotmail.com','redmail.com']

    #     dva=val.split('@')[-1]

    #     if dva not in va :
    #         raise ValueError("Not Found")

    #     return val


def load_db():
    with open('patient.json','r') as f:
        data = json.load(f)

    return data 



@app.get("/")
def home():
    return {"message ":" Patient Management System API "}


@app.get("/about")
def about():
    return {"message":"A fully functional Patient management system API to manage your record "}


@app.get("/view")
def view(patient_id:str=Path(...,description="Id of the patient in DB ",example='P001')):
    d= load_db()


    return d

@app.get("/patient/{p_id}")
def fetch(p_id:str):
    d=load_db()

    if p_id in d:
        return d[p_id]
    raise HTTPException(status_code=404,detail="Pation not found ")


@app.get('/sort')
def sort_p(sort_by:str= Query(...,description="Sort on bases of columns "), order:str=Query(...,description="sort in asc or desc")):

    valid_f=['height','weight','bmi']

    if sort_by not in valid_f:
        raise HTTPException(ststus_code=400,detail=f"Invalid Field selected select from {valid_f}")

    if order not in ['asc','desc']:
        raise HTTPException(ststus_code=400,detail='Invalid order ')

    
    data = load_db()


    sort_ord=True if order == 'desc' else False

    sorted_db=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=f"{sort_ord}")

    return sorted_db
 
