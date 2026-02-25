from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def code_creator(text):
    with open("demo_code.py","w") as code_file:
        code_file.write(text)
        
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
string_parser = StrOutputParser()

template_code = PromptTemplate(
    template="Write a code for the following task\n{task}\nWrite all the non code part as comments in the python code file",
    input_variables=["task"]
)

code_chain = RunnableSequence(template_code,model,string_parser)

parallel_chain=RunnableParallel({
    "code":RunnablePassthrough(),
    "file":RunnableLambda(code_creator)    
})

final_chain=RunnableSequence(code_chain,parallel_chain)

result = final_chain.invoke({"task":"Palindrome of a string"})
print(result["code"])