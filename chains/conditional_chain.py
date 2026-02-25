from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

class Sentiment(BaseModel):
    sentiment:Literal["positive","negative"]=Field(description="This is the sentiment of the feedback")


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
pydantic_parser = PydanticOutputParser(pydantic_object=Sentiment)
str_parser = StrOutputParser()
template_classifier=PromptTemplate(
    template="Classify the sentiment of the feedback as positive or negative\nfeedback:{feedback}\n{format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":pydantic_parser.get_format_instructions()}
)
classifier_chain = template_classifier|model|pydantic_parser

template_positive = PromptTemplate(
    template="Write an appropriate message to this positive feedback\n{feedback}",
    input_variables=["feedback"]
)
template_negative = PromptTemplate(
    template="Write an appropriate message to this negative feedback\n{feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=="positive",template_positive|model|str_parser),
    (lambda x:x.sentiment=="negative",template_negative|model|str_parser),
    RunnableLambda(lambda x:"Couldn't find the sentiment")
)
final_chain =classifier_chain|branch_chain
print(final_chain.invoke({"feedback":"This is a wonderful phone"}))
final_chain.get_graph().print_ascii()