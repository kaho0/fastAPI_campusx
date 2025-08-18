from pydantic import BaseModel,Field
from typing import Optional
class Employee(BaseModel):
    id:int=Field(...,gt=0,title="Employee ID")
    name:str=Field(...,min_length=2)
    department:str=Field(...,min_length=3)
    age:int
    gender:Optional[str]=Field(None,regex="^(Male|Female|Other)$",title="Gender")