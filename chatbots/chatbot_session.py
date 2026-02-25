#Using chatprompttemplate for Dynamic chat prompt templates
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(
    llm=llm
) 
template=ChatPromptTemplate([
    ("system","You are an helpful assistant who's job is to provide crisp on point replies"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{query}")]
)

chat_history=[]
with open("history.txt","r") as f:
    chat_history.extend(f.readlines())

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit": break
    prompt = template.invoke({"chat_history":chat_history,"query": user_input})
    # print(prompt)
    result = model.invoke(prompt)
    print("AI: ", result.content)
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=result.text))

print(chat_history)