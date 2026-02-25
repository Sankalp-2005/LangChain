from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

template1 = PromptTemplate(
    template="You are an research agent, return all the information you have on the topic: {topic}",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template="You are an summarizer agent who's job is to provide summary to the given text in 5 lines \n{text}",
    input_variables=["text"]
)

chain = template1 | model | parser | template2 | model | parser

print(chain.invoke({"topic":input(">")}))