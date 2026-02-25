from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"C:\Users\sj282\OneDrive\Desktop\SJ\AI Agents\LangChain\document_loader\proc&cons.txt",encoding="utf-8")

docs = loader.load()

print(docs)
print(docs[0])
print(docs[0].page_content) # can be sent in a llm to get the output
print(docs[0].metadata)