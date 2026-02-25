from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2"
)

vector =  embedding.embed_query("Hello World")
print(len(vector))
print(str(vector))