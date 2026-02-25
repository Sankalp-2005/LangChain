from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool

class MultiplyInput(BaseModel):
    a:int=Field(description="First number to multiple",required=True)
    b:int=Field(description="Second number to multiple",required=True)
    
def multiply(a:int,b:int)->int:
    """Function to multiply two numbers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: product of two numbers
    """
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="Multiply",
    description="Multiply Two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({"a":3,"b":5})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)
print(multiply_tool.args_schema.model_json_schema())