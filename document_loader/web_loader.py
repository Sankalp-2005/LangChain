from langchain_community.document_loaders import WebBaseLoader

url = "https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/"
loader = WebBaseLoader(
    url #list of urls can also be passed
)
docs =loader.load()

print(docs[0].page_content)