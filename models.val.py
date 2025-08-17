from pydantic import BaseModel,Field
class Employee(BaseModel):
    id:int=Field(...,gt=0)
    name:str=Field(...,min_length=2)
    department:str=Field(...,min_length=3)
    age:int