from fastapi import FastAPI

app=FastAPI()

# static rout 

@app.get("/")
def root():
    return {"msg":"asdfghjklzxcvbnm"}

#dynamic rout

@app.get("/product/{id}")
def get_prod(id: int):
    product=["brush","lapp","monitor","mobile","mouse"]
    return product[id-1]