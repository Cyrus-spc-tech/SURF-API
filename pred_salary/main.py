from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

class ExpInput(BaseModel):
    expInput:float

@app.post("/predict")
def prediction(data:ExpInput):
    #can change this with ML model
    salary = data.expInput*5000+10000

    return {
        "experience": data.expInput,
        "salary":salary
    }