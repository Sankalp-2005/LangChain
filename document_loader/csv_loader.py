from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path=r"C:\Users\sj282\OneDrive\Desktop\SJ\AI Agents\LangChain\document_loader\research-and-development-survey-2024-csv-notes.csv"
)
docs =loader.load()
print(len(docs))
print(docs[0].page_content)