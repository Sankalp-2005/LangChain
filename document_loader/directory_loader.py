from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader =  DirectoryLoader(
    path=r"C:\Users\sj282\OneDrive\Desktop\SJ\AI Agents\LangChain\document_loader\befa_notes",
    loader_cls=PyPDFLoader,
    glob="*.pdf"
)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)
