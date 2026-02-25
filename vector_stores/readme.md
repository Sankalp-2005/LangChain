# LangChain Vector Stores

This module demonstrates **Vector Stores in LangChain**, one of the most important components for building **Retrieval-Augmented Generation (RAG)** systems.

Vector stores allow Large Language Models (LLMs) to retrieve information based on **semantic similarity instead of keyword matching.**

Instead of searching text directly:

```
Keyword Search → Documents
```

Vector stores use embeddings:

```
Query → Embeddings → Vector Search → Documents
```

This module demonstrates **Chroma Vector Database integration with LangChain**, including:

- Document Storage
- Embedding Generation
- Similarity Search
- Metadata Filtering
- Document Updates
- Document Deletion
- Persistent Storage

---

## Overview

Vector stores convert text into **numerical vector representations (embeddings)** and store them in a database for efficient similarity search.

Basic pipeline:

```
Documents
   ↓
Embeddings Model
   ↓
Vector Store
   ↓
Retriever / Search
   ↓
Relevant Documents
```

Vector stores are used in:

- RAG systems
- Chatbots
- Search engines
- AI assistants
- Knowledge bases

---

## Folder Structure

```
vector_stores/
│
├── chroma_vector_db.py
├── chroma_db/
│   ├── chroma.sqlite3
│   ├── header.bin
│   ├── data_level0.bin
│   ├── length.bin
│
└── README.md
```

---

## Vector Store Used

This project uses:

```
Chroma Vector Database
```

Integrated through LangChain.

---

## Example Documents

Documents are stored with metadata. :contentReference[oaicite:0]{index=0}

Example:

```python
Document(
 page_content="Virat Kohli is one of the most successful batsmen...",
 metadata={"Team": "Royal Challengers Bengaluru"}
)
```

Metadata enables filtering during retrieval.

---

## Embeddings Model

Embeddings are generated using:

```
BAAI/bge-m3
```

via:

```python
HuggingFaceEndpointEmbeddings
```

---

## Creating a Vector Store

File:

```
chroma_vector_db.py
```

Vector store initialization: :contentReference[oaicite:1]{index=1}

```python
vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory="chroma_db"
)
```

---

## Persistent Storage

The database is stored locally:

```
chroma_db/
```

Files include:

```
chroma.sqlite3
header.bin
data_level0.bin
length.bin
```

Persistent storage allows:

- Data reuse
- Faster startup
- Production readiness

---

# Operations Supported

This module demonstrates full vector database operations.

---

# 1. Adding Documents

Documents can be added:

```python
vector_store.add_documents(docs)
```

Returns document IDs. :contentReference[oaicite:2]{index=2}

---

## Example Flow

```
Documents
   ↓
Embeddings
   ↓
Stored in Vector DB
```

---

# 2. Fetching Stored Data

Stored data can be retrieved:

```python
vector_store.get(
 include=["embeddings","documents","metadatas"]
)
```

Returns:

- Embeddings
- Documents
- Metadata :contentReference[oaicite:3]{index=3}

---

# 3. Similarity Search

Search for relevant documents:

```python
vector_store.similarity_search(
 query="who among these is a bowler",
 k=2
)
```

Returns the most similar documents. :contentReference[oaicite:4]{index=4}

---

## Similarity Search Pipeline

```
Query
 ↓
Embedding
 ↓
Vector Comparison
 ↓
Top Matches
```

---

# 4. Similarity Search with Scores

Retrieve documents with similarity scores:

```python
vector_store.similarity_search_with_score(
 query="who among these is a bowler",
 k=2
)
```

Returns:

```
(Document, Score)
```

Lower score = closer match. :contentReference[oaicite:5]{index=5}

---

# 5. Metadata Filtering

Search using metadata filters:

```python
vector_store.similarity_search_with_score(
 query="",
 filter={"Team":"Mumbai Indians"}
)
```

Returns documents matching metadata conditions. :contentReference[oaicite:6]{index=6}

---

## Filtering Example

```
Filter:
Team = Mumbai Indians
```

Returns:

```
Rohit Sharma
Jasprit Bumrah
Hardik Pandya
```

---

# 6. Updating Documents

Documents can be updated using document IDs:

```python
vector_store.update_document(
 document_id="document_id_here",
 document=updated_doc
)
```

Updates:

- Content
- Metadata :contentReference[oaicite:7]{index=7}

---

# 7. Deleting Documents

Documents can be deleted:

```python
vector_store.delete(
 ids=["document_id"]
)
```

Removes documents permanently. :contentReference[oaicite:8]{index=8}

---

# Vector Store Architecture

```
Documents
   ↓
Embeddings Model
   ↓
Vector Store (Chroma)
   ↓
Similarity Search
   ↓
Results
```

---

# Installation

Install dependencies:

```bash
pip install langchain
pip install langchain-core
pip install langchain-chroma
pip install langchain-huggingface
pip install chromadb
pip install python-dotenv
```

---

# Environment Setup

Create `.env` file:

```
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
```

---

# Usage

Run:

```
python chroma_vector_db.py
```

Uncomment the desired operation inside the script:

### Add Documents

```python
vector_store.add_documents(docs)
```

---

### Search Documents

```python
vector_store.similarity_search(...)
```

---

### Filter Documents

```python
vector_store.similarity_search(..., filter={})
```

---

### Update Documents

```python
vector_store.update_document(...)
```

---

### Delete Documents

```python
vector_store.delete(...)
```

---

# Modern LangChain Design

This project uses modern LangChain components:

- Chroma Vector Store
- HuggingFace Embeddings
- Document Objects
- Metadata Filtering

No deprecated vector store APIs used.

---

# Key Concepts Learned

## Embeddings

Convert text into vectors:

```
Text → Vector
```

Example:

```
"MS Dhoni" → [0.12, -0.33, 0.88 ...]
```

---

## Vector Search

Similarity search finds closest vectors:

```
Query Vector → Closest Documents
```

---

## Metadata

Extra information attached to documents:

```
Team: Mumbai Indians
```

Used for filtering.

---

## Persistent Storage

Database stored on disk:

```
chroma_db/
```

Allows reuse across sessions.

---

# Real World Applications

Vector stores are used in:

- RAG systems
- Enterprise search
- Document Q&A
- AI assistants
- Knowledge bases
- Semantic search engines

---

# Best Practices

Recommended settings:

```
Chunk Size = 500–1000
Embedding Model = bge-m3 or similar
Top K = 3–5
```

---

# Future Improvements

Possible extensions:

- Pinecone vector store
- FAISS vector store
- Hybrid search
- Re-ranking
- Distributed vector DB
- LangGraph RAG pipelines

---

# Author

LangChain experimentation project focused on learning:

- Vector Databases
- Embeddings
- Retrieval Systems
- RAG Architecture

---

# Notes

Vector stores are the foundation of **Retrieval-Augmented Generation (RAG)** systems.

Most modern AI applications rely on:

```
LLM + Vector Store
```

for accurate and grounded responses.