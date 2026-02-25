from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
string_parser = StrOutputParser()
template_code= PromptTemplate(
    template="Give me the code for the following\n{task}",
    input_variables=["task"]
)
template_explain=PromptTemplate(
    template="Explain the following code\n{code}",
    input_variables=["code"]
)
code_generation_chain=RunnableSequence(template_code,model,string_parser)
parallel_chain=RunnableParallel({
    "code": RunnablePassthrough(),
    "explain": RunnableSequence(code_generation_chain,template_explain,model,string_parser)
})
final_chain = RunnableSequence(code_generation_chain,parallel_chain)
result = final_chain.invoke({"task":"Generate GCD of two numbers"})
print("Code:",result["code"])
print("Explanation:",result["explain"])