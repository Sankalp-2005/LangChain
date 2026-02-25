from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from dotenv import load_dotenv
from pytube import YouTube


load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="BAAI/bge-m3"
)
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

video_id = YouTube(input("Enter the url ")).video_id

try:
    transcript_list = YouTubeTranscriptApi().fetch(video_id)
    text = " ".join(chunk.text for chunk in transcript_list)
except TranscriptsDisabled:
    print("No transcript Found")
    
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
def output_formatter(docs):
    return "\n\n".join(doc.page_content for doc in docs)

chunks = splitter.create_documents([text])

vector_store = FAISS.from_documents(chunks,embeddings)

retriever = vector_store.as_retriever(search_type="similarity",search_kwargs={"k":4})

parallel_chain = RunnableParallel(
    {
        "context":retriever|RunnableLambda(output_formatter),
        "query":RunnablePassthrough()
    }
)

string_parser = StrOutputParser()

template = PromptTemplate(
    template="""You are a helpful assistant
        answer only from the given context:{context}
        and respond to the query:{query}
        if you don't know the answer say 'don't know'
    """,
    input_variables=["context","query"]
)

query = input("User: ")

main_chain = parallel_chain | template | model | string_parser

result = main_chain.invoke(query)

print(result)