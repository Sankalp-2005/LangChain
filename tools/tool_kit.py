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

@tool
def add(a:int,b:int)->int:
    """Function to add two numbers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: addition of two numbers
    """
    return a+b

class MathToolKit:
    def get_tools(self):
        return[add,multiply]
    
toolkit = MathToolKit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name,"->",tool.description)