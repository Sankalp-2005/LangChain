from langchain_core.tools import tool

@tool
def multiply(a:int,b:int)->int:
    """Function to multiply two numbers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: product of two numbers
    """
    return a*b

result = multiply.invoke({"a":3,"b":5})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())