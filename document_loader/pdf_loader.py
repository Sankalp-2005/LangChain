from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\Users\sj282\OneDrive\Desktop\SJ\AI Agents\LangChain\document_loader\test_document.pdf")

docs = loader.load()

print(len(docs))
print(docs[0].page_content)