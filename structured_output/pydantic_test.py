from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class person_details(BaseModel):
    name: str = "User"
    age: int = Field(gt=20,lt=60,default=20, description="Age of a person") #regex is also possible
    address: Optional[str] = None
    email: EmailStr
    
new_person = {
    "name":"Sankalp",
    "age":21,
    "email":"sankalp@gmail.com"
}

new_person1 = {
    "name":56,
    "age":"20", # this works, pydantic supports implicit type conversion but when only data type is defined in the schema and not when field is used
    "email":"sankalp@gmail.com"
}

try:
    person = person_details(**new_person1)
except:
    person = person_details(**new_person)
    
print(person)
person_dict = dict(person)
person_json = person.model_dump_json()

print(person_dict)
print(person_json)