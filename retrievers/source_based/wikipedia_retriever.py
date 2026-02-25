from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)
query = "Ai agents in reinforcement learning"

docs = retriever.invoke(query)

for i,doc in enumerate(docs):
    print(f"---------------------Page content - {i+1}--------------------------")
    print(doc.page_content)