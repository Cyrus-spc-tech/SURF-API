from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ExperienceInput(BaseModel):
    exp: float

@app.post("/predict")
def predict_salary(data: ExperienceInput):
    salary = data.exp * 5000 + 10000
    return {
        "experience": data.exp,
        "predicted_salary": salary
    }
