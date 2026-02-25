from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\Users\sj282\OneDrive\Desktop\SJ\AI Agents\LangChain\text_splitters\test_document.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    separator="",
    chunk_size = 500,
    chunk_overlap =0,
    is_separator_regex=False
)

result = splitter.split_documents(docs)

print(result[0])