from langchain_core.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a:int=Field(description="First number to multiple",required=True)
    b:int=Field(description="Second number to multiple",required=True)
    
class Multiply(BaseTool):
    name : str = "Multiply"
    description:str="Multiply two numbers"
    args_schema:type[BaseModel]=MultiplyInput
    def _run(self,a:int,b:int)->int:
        return a*b
    
multiply_tool = Multiply()
result = multiply_tool.invoke({"a":3,"b":5})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)
print(multiply_tool.model_json_schema)