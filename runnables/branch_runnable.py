from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableBranch
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
string_parser = StrOutputParser()

template_text_generator = PromptTemplate(
    template="Write a detailed report on the topic:{topic}",
    input_variables=["topic"]
)
template_summarizer = PromptTemplate(
    template="Write a summary on text:{text}",
    input_variables=["text"]
)

text_generator = RunnableSequence(template_text_generator,model,string_parser)

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>500, RunnableSequence(template_summarizer,model,string_parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(text_generator,branch_chain)
result =  final_chain.invoke({"topic":"Engineer"})
print(result)
final_chain.get_graph().print_ascii()