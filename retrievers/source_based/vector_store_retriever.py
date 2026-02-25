from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="BAAI/bge-m3"
)

doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in modern cricket. Known for his aggressive playing style and exceptional fitness, he has led India across all formats. Kohli has scored over 25,000 international runs and is widely regarded as one of the greatest chasers in limited-overs cricket."
)
doc2 = Document(
    page_content="Rohit Sharma, popularly known as the “Hitman,” is famous for his elegant stroke play and ability to score big hundreds. He holds the record for the highest individual score in ODIs (264 runs). Rohit has captained India in multiple formats and has led Mumbai Indians to several IPL titles."
)
doc3 = Document(
    page_content="Jasprit Bumrah is India’s premier fast bowler, known for his unique bowling action and deadly yorkers. He has been instrumental in India’s victories in Test matches overseas and is considered one of the best death-over specialists in T20 cricket."
)
doc4 = Document(
    page_content="MS Dhoni is one of India’s most successful captains, having led the team to victory in the 2007 T20 World Cup, 2011 ODI World Cup, and 2013 Champions Trophy. Known for his calm demeanor and finishing abilities, Dhoni revolutionized Indian cricket leadership."
)
doc5 = Document(
    page_content="Hardik Pandya is a dynamic all-rounder known for his explosive batting and effective medium-pace bowling. He has played crucial roles in India’s white-ball cricket success and is valued for his versatility and athletic fielding."
)

docs = [doc1,doc2,doc3,doc4,doc5]

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="sample"
)

retriever = vector_store.as_retriever(search_kwargs={"k":2})

query="Who is MS Dhoni"
result = retriever.invoke(query)

for i,doc in enumerate(result):
    print(f"-----------------------------Result - {i+1} ---------------------------------")
    print(doc.page_content)