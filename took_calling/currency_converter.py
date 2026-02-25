from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import InjectedToolArg
from langchain_core.messages import HumanMessage
from typing import Annotated
from langchain_core.tools import tool
from dotenv import load_dotenv
import requests
import json
import os 

load_dotenv()

api_key = os.getenv("Exchange_rate_api_key")

@tool
def get_conversion_factor(base_currency:str, target_currency:str)->float:
    """This function fetches the conversion factor between the two provided currencies, one being base currency other being the target currency using the exchange rate api

    Args:
        base_currency (str): The base currency from which the conversion is to be done
        target_currency (str): The target currency to which the conversion is to be done

    Returns:
        float: The conversion factor between the base and the target currency.
    """
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    result = requests.get(url)
    return result.json()


@tool
def convert(amount:int,rate:Annotated[float,InjectedToolArg])->float:
    """Function to return currency value based on conversion rate

    Args:
        amount (float): first number, the amount to be converted
        rate (int): second number, conversion rate which is to be used to convert the amount

    Returns:
        int: product of two numbers
    """
    return amount*rate

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

model_with_tools = model.bind_tools([get_conversion_factor,convert])

messages = [HumanMessage(input("User: "))]

ai_message = model_with_tools.invoke(messages)

messages.append(ai_message)

for tool_call in ai_message.tool_calls:
    if tool_call["name"]=="get_conversion_factor":
        tool_message_1 = get_conversion_factor.invoke(tool_call)
        conversion_rate = json.loads(tool_message_1.content)["conversion_rate"]
        messages.append(tool_message_1)
    elif tool_call["name"]=="convert":
        tool_call["args"]["conversion_rate"] = conversion_rate
        tool_message_2 = convert.invoke(tool_call)
        messages.append(tool_message_2)

final_result = model_with_tools.invoke(messages)
print("AI: ",final_result.content)