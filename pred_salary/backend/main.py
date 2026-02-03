from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("pred_salary_model.pkl")

class ExperienceInput(BaseModel):
    exp: float

@app.post("/predict")
def predict_salary(data: ExperienceInput):
    prediction = model.predict(np.array([[data.exp]]))
    return {
        "experience": data.exp,
        "predicted_salary": float(prediction[0])
    }
