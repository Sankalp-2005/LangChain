# LangChain Retrievers (Source-Based)

This module demonstrates how to use **Source-Based Retrievers in LangChain**.

Retrievers allow Large Language Models (LLMs) to fetch **relevant information from external sources** before generating responses. They are a core building block of **Retrieval-Augmented Generation (RAG)** systems.

This folder focuses on **source-based retrievers**, where information is retrieved directly from structured or external data sources instead of prompting the LLM alone.

Covered retrievers:

- Vector Store Retriever (Embeddings-Based)
- Wikipedia Retriever (API-Based)

---

## Overview

Large Language Models do not have reliable real-time knowledge and may hallucinate information.

Retrievers solve this problem by:

- Fetching relevant documents
- Providing factual context
- Reducing hallucinations
- Enabling knowledge-based responses

Typical Retrieval Pipeline:

```
User Query
   ↓
Retriever
   ↓
Relevant Documents
   ↓
LLM
   ↓
Answer grounded in sources
```

This folder focuses on **retrieval only**, not full RAG pipelines.

---

## Files

```
retrievers/
│
├── vector_store_retriever.py
├── wikipedia_retriever.py
│
└── README.md
```

---

## 1. Vector Store Retriever

File:

```
vector_store_retriever.py
```

This example demonstrates how to build a **Vector Store Retriever using embeddings and ChromaDB**.

Documents are embedded into vector space and similarity search is used to retrieve the most relevant documents.

The retriever returns the **top-k most similar documents**. :contentReference[oaicite:0]{index=0}

---

### Architecture

```
Documents
   ↓
Embeddings Model
   ↓
Vector Store (Chroma)
   ↓
Retriever
   ↓
Relevant Documents
```

---

### Implementation Steps

#### Step 1 — Create Documents

```python
from langchain_core.documents import Document
```

Documents contain text content:

```python
doc1 = Document(page_content="Virat Kohli is one of the most successful batsmen...")
```

Multiple documents are combined:

```python
docs = [doc1, doc2, doc3, doc4, doc5]
```

---

#### Step 2 — Create Embeddings Model

```python
from langchain_huggingface import HuggingFaceEndpointEmbeddings
```

```python
embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="BAAI/bge-m3"
)
```

The embedding model converts text into numerical vectors.

---

#### Step 3 — Create Vector Store

```python
from langchain_community.vectorstores import Chroma
```

```python
vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="sample"
)
```

The vector store stores embeddings for similarity search. :contentReference[oaicite:1]{index=1}

---

#### Step 4 — Create Retriever

```python
retriever = vector_store.as_retriever(
    search_kwargs={"k":2}
)
```

Parameter:

| Parameter | Meaning |
|---------|---------|
| k | Number of documents to retrieve |

---

#### Step 5 — Query Retriever

```python
result = retriever.invoke(query)
```

The retriever returns the most relevant documents. :contentReference[oaicite:2]{index=2}

---

### Example Query

```
Who is MS Dhoni
```

Example Output:

```
MS Dhoni is one of India's most successful captains...
```

---

### Key Concepts

#### Embeddings

Embeddings convert text into vectors:

```
Text → Vector Representation
```

Example:

```
"MS Dhoni" → [0.12, -0.44, 0.88, ...]
```

Similar text produces similar vectors.

---

#### Similarity Search

Retriever finds documents with closest vectors:

```
Query Vector
   ↓
Compare with Stored Vectors
   ↓
Return Top Matches
```

---

### Use Cases

- Knowledge bases
- Search engines
- Chatbots
- Document retrieval
- RAG pipelines
- FAQ systems

---

## 2. Wikipedia Retriever

File:

```
wikipedia_retriever.py
```

This example demonstrates how to retrieve documents directly from **Wikipedia** using LangChain's built-in retriever. :contentReference[oaicite:3]{index=3}

Unlike vector stores, this retriever fetches **live information from an external source**.

---

### Architecture

```
User Query
   ↓
Wikipedia Retriever
   ↓
Wikipedia API
   ↓
Documents
```

---

### Implementation

#### Step 1 — Create Retriever

```python
from langchain_community.retrievers import WikipediaRetriever
```

```python
retriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)
```

Parameters:

| Parameter | Meaning |
|---------|---------|
| top_k_results | Number of pages returned |
| lang | Wikipedia language |

---

#### Step 2 — Query Retriever

```python
docs = retriever.invoke(query)
```

The retriever returns Wikipedia page content. :contentReference[oaicite:4]{index=4}

---

### Example Query

```
AI agents in reinforcement learning
```

Example Output:

```
Reinforcement learning is an area of machine learning...
```

---

### Key Concepts

#### API-Based Retrieval

Instead of embeddings:

```
Query → Wikipedia API → Documents
```

Advantages:

- Real information
- No database setup
- Fresh content

---

### Use Cases

- Research assistants
- Educational bots
- Fact-based Q&A
- Real-time knowledge retrieval

---

## Vector Store vs API Retrievers

| Feature | Vector Store Retriever | Wikipedia Retriever |
|---------|------------------------|---------------------|
| Data Source | Custom Documents | Wikipedia |
| Setup Required | Yes | No |
| Embeddings | Required | Not Required |
| Speed | Very Fast | Network Dependent |
| Custom Knowledge | Yes | No |
| Real-Time Data | No | Yes |

---

## Installation

### 1. Install Dependencies

```bash
pip install langchain
pip install langchain-core
pip install langchain-community
pip install langchain-huggingface
pip install chromadb
pip install python-dotenv
```

---

## Environment Setup

Create `.env` file:

```
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
```

---

## Usage

### Vector Store Retriever

Run:

```bash
python vector_store_retriever.py
```

Example Output:

```
Result 1:
MS Dhoni is one of India's most successful captains...

Result 2:
Rohit Sharma is famous for elegant stroke play...
```

---

### Wikipedia Retriever

Run:

```bash
python wikipedia_retriever.py
```

Example Output:

```
Page Content 1:
Reinforcement learning is a machine learning paradigm...

Page Content 2:
AI agents are entities that perceive environments...
```

---

## Modern LangChain Design

This project uses **modern LangChain retriever architecture:**

- VectorStoreRetriever
- Runnable-compatible retrievers
- Embedding-based search
- API-based retrieval

No deprecated components used.

---

## Key Concepts Learned

### Retriever

A retriever returns documents relevant to a query:

```
Query → Retriever → Documents
```

---

### Vector Store Retrieval

```
Documents → Embeddings → Vector Store → Retriever → Results
```

---

### Source-Based Retrieval

Instead of relying only on the LLM:

```
LLM + External Knowledge
```

This significantly improves factual accuracy.

---

## Real World Applications

### Vector Store Retrieval

- Enterprise knowledge bases
- Internal documentation search
- Customer support bots
- Legal document search
- Medical search systems

---

### Wikipedia Retrieval

- Research assistants
- Educational tools
- AI tutors
- Fact-checking systems

---

## Future Improvements

Possible extensions:

- Hybrid search (BM25 + Embeddings)
- RAG pipelines
- Multi-retriever routing
- Parent document retrievers
- Contextual compression retrievers
- Self-query retrievers
- LangGraph RAG systems

---

## Author

LangChain experimentation project focused on learning:

- Retrievers
- RAG Systems
- Vector Databases
- Embeddings
- Modern LangChain Architecture

---

## Notes

This module focuses on **practical retriever implementations** used in real-world AI systems.

Retrievers are one of the most important components in building **production-grade LLM applications.**