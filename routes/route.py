from fastapi import APIRouter,Response
from config.db import collection_name
from schema.sch import list_serial
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional

router=APIRouter()




class Address(BaseModel):
    city: str
    country: str


class Stud(BaseModel):
    name: str
    age: int
    address: Address





@router.post("/api/students")
async def add_student(stud:Stud,response:Response):
    stud_dict = stud.dict()
    stud_dict['address'] = stud.address.dict()
    result=collection_name.insert_one(stud_dict)
    response.status_code=201
    return {"id":str(result.inserted_id)}


@router.get("/api/students")
async def get_students(response:Response,country:Optional[str]=None,age:Optional[int]=None):
    if(country==None and age==None):
        todos=list_serial(collection_name.find())
    elif(country==None):
        todos=list_serial(collection_name.find({"age": {"$gt": age-1}}))
    elif(age==None):
        todos=list_serial(collection_name.find({"address.country":country}))
    else:
        todos=list_serial(collection_name.find({"address.country":country,"age": {"$gt": age-1}}))
        
    data=[]
    for todo in todos:
        dict={
            "name":todo["name"],
            "age":todo["age"]
        }
        data.append(dict)
    response.status_code=200
    return {"data":data}

@router.get("/api/students/{id}")
async def get_student_with_id(id:str,response:Response):
    obj_id = ObjectId(id)
    result=list_serial(collection_name.find({"_id":obj_id}))
    result[0].pop("id")
    response.status_code=200
    return result[0]

@router.patch("/api/students/{id}")
async def update_student_details(id:str,stud:Stud,response:Response):
    id = ObjectId(id)
    result=collection_name.update_one({"_id":id},{"$set":stud.dict()})
    response.status_code=204
    return {}

@router.delete("/api/students/{id}")
async def delete_student(id:str,response:Response):
    id=ObjectId(id)
    result=collection_name.delete_one({"_id":id})
    response.status_code=200
    return {}
