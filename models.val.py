from pydantic import BaseModel,Field
class Employee(BaseModel):
    id:int=Field(...,gt=0)
    name:str
    department:str
    age:int