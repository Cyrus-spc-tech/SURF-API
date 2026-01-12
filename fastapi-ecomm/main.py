from app.services.products import get_all_prod
from fastapi import FastAPI 

app = FastAPI()

@app.get("/product")
def get_prod():
    return get_all_prod()