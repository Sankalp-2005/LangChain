from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
# from langchain_core.prompts import ChatPromptTemplate ---- Do this for Dynamic chat prompt templates

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(
    llm=llm
) 
history = [
    SystemMessage(content="You are an helpful assistant who's job is to provide crisp on point replies")
]
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit": break
    history.append(HumanMessage(content=user_input))
    result = model.invoke(history)
    history.append(AIMessage(content=result.content))
    print("AI: ", result.content)
    
print(history) #here the history can be stored somewhere as txt or in data base which can be then included in chatbot_session.py file where we can have the track of the sessions