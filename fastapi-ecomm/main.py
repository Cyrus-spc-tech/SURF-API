from app.services.products import get_all_prod
from fastapi import FastAPI , HTTPException, Query

app = FastAPI()

@app.get("/product")
def get_prod():
    return get_all_prod()


@app.get("/product")
def list_prod(name: str = Query(default = None,min_length=1,max_length=50,description="Serch ny product name : ")):
    return name