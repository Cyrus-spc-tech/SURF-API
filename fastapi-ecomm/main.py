from app.services.products import get_all_prod
from fastapi import FastAPI , HTTPException, Query

app = FastAPI()

# @app.get("/product")
# def get_prod():
#     return get_all_prod()

@app.get("/")
def root():
    return {"msg":"Hello there how u doing "}


@app.get("/product")
def list_prod(
    name: str = Query(default=None, 
    min_length=1, 
    max_length=50, 
    description="Search for a product name: "
    ),

    sort_by_price:bool =Query(default=False,description="Sort product by price "
    ),

    order:str = Query(default="asc",description="Sort order by (asc,desc)"),

    limit:int=Query(default=5, 
    ge=1, 
    le=100, 
    description="Limit of item")

):
    products = get_all_prod()

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]
    
    if not products:
        raise HTTPException(
            status_code=404,
            detail=f"No product match with the name '{name}'",
        )


    if sort_by_price:
        reverse =order =="desc"
        products=sorted(products,key=lambda p : p.get("price",0),reverse=reverse)
    


    total = len(products)
    products = products[0:limit]
    




    return {"total": total,"fetched ":limit, "items": products}