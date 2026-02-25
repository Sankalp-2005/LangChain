from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field

class Movie(BaseModel):
    Dicrector : list[str] =Field(description="List of names of directors of the movie")
    Actor : list[str]=Field(description="List of names of actors in the movie")
    Producer : list[str]=Field(description="List of names of producers of the movie")
    
load_dotenv()

llm =  HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
parser = PydanticOutputParser(pydantic_object=Movie)
template = PromptTemplate(
    template="Give me the names of the Directors, Actors and Producers of the Movie: {movie}\n{format_instruction}",
    input_variables=["movie"],
    partial_variables={"format_instruction":parser.get_format_instructions}
)
chain = template|model|parser
print(chain.invoke({"movie":"Titanic"}))
