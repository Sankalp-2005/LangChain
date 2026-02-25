from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

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

query = HumanMessage("What is 3 multiplied by 10")

messages = [query]

#Tool Binding

model_with_tool = model.bind_tools([multiply])

result_ai = model_with_tool.invoke(messages)

messages.append(result_ai)

#Tool Execution

result_tool = multiply.invoke(result_ai.tool_calls[0])

messages.append(result_tool)

final_result = model_with_tool.invoke(messages)

print(final_result.content)