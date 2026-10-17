from fastapi import FastAPI,Path,HTTPException
import json
from pydantic import BaseModel,Field
from typing import Annotated,Literal


app = FastAPI()

def load_data():
    with open('dat.json','r') as f:
        data = json.load(f)
    return data

class Patient(BaseModel):

    id = Annotated [str,Field(...,description="Id of patient",examples='P001')]
    name = Annotated[str,Field(...,description="Name of patinet",examples= "Raj Lodh")]
    age = Annotated[int,Field(...,description="Age of patient",examples="0 to 120")]


@app.get("/")
def hello():
    return ('Hello world')

@app.get("/view")
def paitent_data():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_data(patient_id:str =Path(...,description="Patient Id in db",example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException (status_code=404,detail="Patient ID not found")

@app.post('/create')
def create(patient:Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient already exist")
    data[paitent.id] = patient.model_dump(exclude=['id'])
    save_data(data)