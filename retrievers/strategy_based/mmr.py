# MMR stands for Maximal Marginal Relevance
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="BAAI/bge-m3"
)


docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embeddings
)
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs = {"k":3,"lambda_mult":0}
)
query = "What is Langchain"
result = retriever.invoke(query)
for i,doc in enumerate(result):
    print(f"----------------------Result - {i+1}--------------------------")
    print(doc.page_content)