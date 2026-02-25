from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import  JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name of director, producer, actors of the given movie: \n{movie}\n{format_instruction}",
    input_variables=["movie"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)
# prompt = template.invoke({"movie":"GodFather"})
# result = model.invoke(prompt)
# print(result.content)
# parsed = parser.parse(result.content)
# print(parsed)

chain = template | model | parser # Above Commented code using chains

print(chain.invoke({"movie":"Titanic"}))