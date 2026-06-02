import pandas as pd
import numpy as np 
from typing import Literal,Annotated
from fastapi import FastAPI,Path,Query,HTTPException,JSONResponse
from pydantic import BaseModel,Field,computed_field
import pickle



with open('model.pkl','rb') as f:
    model=pickle.load(f)

app=FastAPI()



# to validate incomming data

class UserInput(BaseModel):
    age:Annotated[int,Field(...,gt=0,lt=120,description="Age of the User")]
    weight:Annotated[float,Field(...,description="weight of the User")]
    height:Annotated[float,Field(...,description="height of the User")]
    income:Annotated[float,Field(...,gt=0,description="Income of the User")]
    smoker:Annotated[bool,Field(...,description="smoker or not ")]
    city:Annotated[str,Field(...,gt=0,lt=120,description="city of the User")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'], Field( ... , description='Occupation of the user')]

@computed_field
@property
def bmi(self)-> float :
    return self.weigth/(self.height**2)


@computed_field
@property
def life_risk(self)->str:
    if self.smoker and self.bmi>30 :
        return "high"
    elif self.smoker and self.bmi >27:
        return "medium"

    else:
        return "low"


@computed_field
@property
def     
cd 
