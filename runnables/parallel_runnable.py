from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

template_manual = PromptTemplate(
    template="Generate a manual code for the following task\n{task}",
    input_variables=["task"]
)
template_inbuilt = PromptTemplate(
    template="Generate a code using builtin functions for the following task\n{task}",
    input_variables=["task"]
)
parser = StrOutputParser()
parallel_chain = RunnableParallel(
    {
        "manual":RunnableSequence(template_manual|model|parser),
        "inbuilt":RunnableSequence(template_inbuilt|model|parser)
    }
)

 
result = parallel_chain.invoke({"task":"Find the gcd of two numbers"})
print("Manual Code:\n", result["manual"])
print("Code using Inbuilt Functions:\n", result["inbuilt"])