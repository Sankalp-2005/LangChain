from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="BAAI/bge-m3"
)

doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in modern cricket. Known for his aggressive playing style and exceptional fitness, he has led India across all formats. Kohli has scored over 25,000 international runs and is widely regarded as one of the greatest chasers in limited-overs cricket.",
    metadata={"Team": "Royal Challengers Bengaluru"}
)
doc2 = Document(
    page_content="Rohit Sharma, popularly known as the “Hitman,” is famous for his elegant stroke play and ability to score big hundreds. He holds the record for the highest individual score in ODIs (264 runs). Rohit has captained India in multiple formats and has led Mumbai Indians to several IPL titles.",
    metadata={"Team": "Mumbai Indians"}
)
doc3 = Document(
    page_content="Jasprit Bumrah is India’s premier fast bowler, known for his unique bowling action and deadly yorkers. He has been instrumental in India’s victories in Test matches overseas and is considered one of the best death-over specialists in T20 cricket.",
    metadata={"Team": "Mumbai Indians"}
)
doc4 = Document(
    page_content="MS Dhoni is one of India’s most successful captains, having led the team to victory in the 2007 T20 World Cup, 2011 ODI World Cup, and 2013 Champions Trophy. Known for his calm demeanor and finishing abilities, Dhoni revolutionized Indian cricket leadership.",
    metadata={"Team": "Chennai Super Kings"}
)
doc5 = Document(
    page_content="Hardik Pandya is a dynamic all-rounder known for his explosive batting and effective medium-pace bowling. He has played crucial roles in India’s white-ball cricket success and is valued for his versatility and athletic fielding.",
    metadata={"Team": "Mumbai Indians"}
)

docs = [doc1,doc2,doc3,doc4,doc5]

vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory="chroma_db"
)

#----------------------------------add documents ----------------------------------
# good to comment during reruns to avoid storing data again in the database

# result_add = vector_store.add_documents(docs) 
# print(result_add) # Returns the embeddings id of the documents

# ----------------------------------To fetch embeddings, documents, metadata ----------------------------------
# result_search = vector_store.get(include=["embeddings","documents","metadatas"]) 
# print(result_search) 

# ---------------------------------- Search document ----------------------------------
# result_similarity_search = vector_store.similarity_search(        
#     query="who among these is a bowler",
#     k=2
# )
# print(result_similarity_search)

# ----------------------------------Search document with similarity score ----------------------------------

# result_with_similarity_score = vector_store.similarity_search_with_score(        
#     query="who among these is a bowler",
#     k=2
# )
# print(result_with_similarity_score)

# ----------------------------------Search by filtering using metadata----------------------------------

# result_filtering = vector_store.similarity_search_with_score(          
#     query="",
#     filter={"Team":"Mumbai Indians"}
# )
# print(result_filtering) 


# ----------------------------------Update documents using document_id ----------------------------------

# updated_doc1 = Document(
#     page_content="Virat Kohli[a] (born 5 November 1988) is an Indian international cricketer and the former all-format captain of the Indian national cricket team.[3] He is a right-handed batter and occasional right-arm medium pace bowler.",
#     metadata={"Team": "Royal Challengers Bengaluru"}
# )

# vector_store.update_document(
#     document_id="ebcef6fc-94dc-47d5-98d7-b038c921a5c9",
#     document=updated_doc1
# )

# To fetch embeddings, documents, metadata of the updated 

# result_updated = vector_store.get(include=["embeddings","documents","metadatas"]) 
# print(result_updated) 

# ----------------------------------Delete documents using document_id ----------------------------------

# vector_store.delete(ids=["ebcef6fc-94dc-47d5-98d7-b038c921a5c9"])

# To fetch embeddings, documents, metadata after deletion

# result_deletion = vector_store.get(include=["embeddings","documents","metadatas"]) 
# print(result_deletion) 