



from fastapi import FastAPI , Path , HTTPException , Query
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel ,Field,computed_field    # field_validator # EmailStr  >> email : EmailStr   # AnyUrl   
from typing import List,Dict,Optional,Annotated,Literal



app = FastAPI()


class Address(BaseModel):
    state:str
    city:str
    pin:str

class Patient(BaseModel):

    id:Annotated[str,Field(default=..., description="ID of the Patient", example=['P001'])]
    name: Annotated[str,Field(default=..., description="Name of the Patient ")]
    age : Annotated[int,Field(default=..., description="Age of the Patient ")]
    gender:Annotated[Literal['Male','Female'],Field(default=..., description="Gender of the Patient")]
    height:Annotated[float,Field(default=..., description="Height of the Patient in mtrs")]
    weight:Annotated[float,Field(default=..., description="Weight of the Patient in kgs")]
    address: Address


    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)

        return bmi

    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi<18.5:
            return 'UnderWeight'
        elif self.bmi <25:
            return 'Normal'
        else:
            return 'OverWeight'


class PatientUpdate(BaseModel):
    name:  Annotated[Optional[str],Field(default=..., description="Name of the Patient ")]
    age :  Annotated[Optional[int],Field(default=..., description="Age of the Patient ")]
    gender:Annotated[Optional[Literal['Male','Female']],Field(default=..., description="Gender of the Patient")]
    height:Annotated[Optional[float],Field(default=..., description="Height of the Patient in mtrs")]
    weight:Annotated[Optional[float],Field(default=..., description="Weight of the Patient in kgs")]
    address: Address


    # @field_validator('email')
    # @classmethod
    # def email_verify(cls,val):
    #     va=['gmail.com','hotmail.com','redmail.com']

    #     dva=val.split('@')[-1]

    #     if dva not in va :
    #         raise ValueError("Not Found")

    #     return val


def load_db():
    with open('patient.json','r') as f:
        data = json.load(f)

    return data 

def save_db(data):
    with open('patient.json','w') as f:
        json.dump(data,f)



@app.get("/")
def home():
    return {"message ":" Patient Management System API "}


@app.get("/about")
def about():
    return {"message":"A fully functional Patient management system API to manage your record "}


@app.get("/view")
def view(patient_id:str=Path(...,description="Id of the patient in DB ",example='P001')):
    d= load_db()


    return d

@app.get("/patient/{p_id}")
def fetch(p_id:str):
    d=load_db()

    if p_id in d:
        return d[p_id]
    raise HTTPException(status_code=404,detail="Pation not found ")


@app.get('/sort')
def sort_p(sort_by:str= Query(...,description="Sort on bases of columns "), order:str=Query(...,description="sort in asc or desc")):

    valid_f=['height','weight','bmi']

    if sort_by not in valid_f:
        raise HTTPException(status_code=400,detail=f"Invalid Field selected select from {valid_f}")

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order ')

    
    data = load_db()


    sort_ord=True if order == 'desc' else False

    sorted_db=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_ord)

    return sorted_db
 
@app.post("/create")
def create_patent(patient: Patient):
    #load data 
    data=load_db()

    #check if exist
    if patient.id in data :
        return HTTPException(status_code=400,detail='Patient Alredy Exist')
   
    data[patient.id]=patient.model_dump(exclude={'id'}) #dict fix

    save_db(data)


    return JSONResponse(status_code=201,content={'message':'Patient has been Created '})


@app.put("/update/{patientid}")
def update_patient(patient_id:str,patient_upt:PatientUpdate):
    data=load_db()

    if patient_id not in data:
        return HTTPException(status_code=404,detail='Patient id not Found ')


    exist_d=data[patient_id]

    newinfo=patient_upt.model_dump(exclude_unset=True)# only sent by client

    for key,value in newinfo.items():
        exist_d[key]=value

        # existing patient >> pydantic obj >> updated bmi +verdict >> pydantic obj >> dict
         
        exist_d['id']=patient_id
        pyd_patient=Patient(**exist_d) 

        exist_d=pyd_patient.model_dump(exclude='id')

        data[patient_id]=exist_d

        save_db(data)
        return JSONResponse(status_code=200,content={'message':"Patient Updtaed"})




@app.delete("/delete/{patient_id}")
def delete_patient(patient_id:str):
    data = load_db()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Patient not Found ')

    del data[patient_id]

    save_db(data)

    return JSONResponse(status_code=200,content={'message':'Patient Deleted '})

    