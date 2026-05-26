from fastapi import FastAPI 
import json



app = FastAPI()

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
def view():
    d= load_db()


    return d

@app.get("/patient/{p_id}")
def fetch(p_id:str):
    d=load_db()

    if p_id in d:
        return d[p_id]
    return {"message":"No Record Found "}
