from app.services.products import get_all_prod
from fastapi import FastAPI , HTTPException, Query

app = FastAPI()

# @app.get("/product")
# def get_prod():
#     return get_all_prod()


@app.get("/product")
def list_prod(
    name: str = Query(default=None, min_length=1, max_length=50, description="Search for a product name: ")
):
    products = get_all_prod()

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    total = len(products)
    if not products:
        raise HTTPException(
            status_code=404,
            detail=f"No product match with the name '{name}'",
        )

    return {"total": total, "items": products}