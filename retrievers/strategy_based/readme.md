# LangChain Retrievers (Strategy-Based)

This module demonstrates **Strategy-Based Retrievers in LangChain**.

Unlike source-based retrievers (VectorStore, Wikipedia, etc.), strategy-based retrievers focus on **how documents are retrieved**, not **where they come from**.

Retrieval strategies improve:

- Relevance
- Diversity
- Accuracy
- Context Quality
- LLM Performance

This folder covers important retrieval strategies used in real-world **RAG (Retrieval-Augmented Generation)** systems.

Covered strategies:

- Maximal Marginal Relevance (MMR)
- Multi Query Retrieval (Conceptual)
- Contextual Compression Retrieval (Conceptual)

---

## Overview

Basic retrieval works like this:

```
Query → Retriever → Top-K Documents
```

Strategy-based retrieval improves this pipeline:

```
Query
  ↓
Retrieval Strategy
  ↓
Improved Documents
  ↓
LLM
```

These strategies are critical for building **high-quality RAG systems**.

---

## Folder Structure

```
retrievers_strategy/
│
├── mmr.py
├── multi_query_retriever.py
├── contextual_compression_retrievers.py
│
└── README.md
```

---

## Retrieval Strategies Covered

| Strategy | Purpose | Status |
|---------|---------|--------|
| MMR Retriever | Diverse document retrieval | Implemented |
| Multi Query Retriever | Query expansion retrieval | Conceptual |
| Contextual Compression Retriever | Reduce irrelevant context | Conceptual |

---

# 1. MMR Retriever (Maximal Marginal Relevance)

File:

```
mmr.py
```

MMR stands for **Maximal Marginal Relevance**.

It is a retrieval strategy that balances:

- Relevance to the query
- Diversity among results

Basic similarity search often returns **very similar documents**.

MMR ensures the results are **different but still relevant**. :contentReference[oaicite:0]{index=0}

---

## Why MMR is Important

Normal similarity search:

```
Query: "What is LangChain"

Results:

1. LangChain is a framework...
2. LangChain is used for...
3. LangChain helps build...
```

These results are redundant.

---

MMR Search:

```
Query: "What is LangChain"

Results:

1. LangChain overview
2. Embeddings explanation
3. Vector stores explanation
```

More useful context for LLMs.

---

## Architecture

```
Documents
   ↓
Embeddings
   ↓
Vector Store (FAISS)
   ↓
MMR Retrieval
   ↓
Diverse Documents
```

---

## Implementation

### Step 1 — Create Documents

```python
from langchain_core.documents import Document
```

Example:

```python
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="Embeddings are vector representations of text."),
]
```

---

### Step 2 — Create Embeddings

```python
from langchain_huggingface import HuggingFaceEndpointEmbeddings
```

```python
embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="BAAI/bge-m3"
)
```

---

### Step 3 — Create Vector Store

```python
from langchain_community.vectorstores import FAISS
```

```python
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embeddings
)
```

FAISS stores vector embeddings for similarity search. :contentReference[oaicite:1]{index=1}

---

### Step 4 — Create MMR Retriever

```python
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":3,
        "lambda_mult":0
    }
)
```

Parameters:

| Parameter | Meaning |
|---------|---------|
| k | Number of documents |
| lambda_mult | Relevance vs diversity tradeoff |

---

### Lambda Parameter

```
lambda_mult = 1
```

Maximum relevance

```
lambda_mult = 0
```

Maximum diversity

Example in this project:

```python
lambda_mult = 0
```

Prioritizes diversity. :contentReference[oaicite:2]{index=2}

---

### Step 5 — Query Retriever

```python
result = retriever.invoke(query)
```

Example Query:

```
What is LangChain
```

Example Output:

```
LangChain makes it easy to work with LLMs.

Embeddings are vector representations of text.

MMR helps you get diverse results...
```

---

## When to Use MMR

Use MMR when:

- Documents are repetitive
- Context window is limited
- Need diverse information
- Building RAG systems
- Summarization pipelines

---

# 2. Multi Query Retriever (Concept)

File:

```
multi_query_retriever.py
```

Multi Query Retrieval improves retrieval by generating **multiple variations of the same query**.

Example:

```
Original Query:
"What is LangChain"
```

Generated Queries:

```
What is LangChain?
Explain LangChain framework
LangChain overview
Uses of LangChain
```

Each query retrieves documents.

Results are merged.

---

## Architecture

```
User Query
   ↓
LLM Query Generator
   ↓
Multiple Queries
   ↓
Retriever
   ↓
Merged Documents
```

---

## Status

This retriever is currently **not implemented in this module**.

It exists in older LangChain versions and is now part of **LangChain Classic (legacy)**. :contentReference[oaicite:3]{index=3}

Future versions can implement this using **LangChain Expression Language (LCEL)**.

---

## Why Multi Query Retrieval Matters

Basic retrieval may miss documents:

```
Query:
"LLM agents"
```

But documents might contain:

```
Autonomous AI systems
```

Multi-query retrieval solves this.

---

## Use Cases

- Research assistants
- Semantic search
- Knowledge bases
- Complex queries
- RAG pipelines

---

# 3. Contextual Compression Retriever (Concept)

File:

```
contextual_compression_retrievers.py
```

Contextual Compression reduces irrelevant information inside retrieved documents.

Instead of returning full documents:

```
Retriever → Full Documents
```

It returns only relevant sections:

```
Retriever → Compressor → Relevant Text
```

---

## Architecture

```
Query
  ↓
Retriever
  ↓
Documents
  ↓
Compressor
  ↓
Relevant Sections
```

---

## Status

This retriever is currently **not implemented in this module**.

It exists in older LangChain versions and is now part of **LangChain Classic (legacy)**. :contentReference[oaicite:4]{index=4}

Future implementations can use:

- LLM-based compression
- Token filtering
- Re-ranking models

---

## Why Contextual Compression Matters

LLMs have limited context windows.

Without compression:

```
5 Documents × 1000 tokens = 5000 tokens
```

With compression:

```
Relevant text only = 800 tokens
```

Better performance and lower cost.

---

## Strategy Comparison

| Strategy | Goal | Advantage | Complexity |
|---------|------|-----------|------------|
| Similarity Search | Relevant docs | Simple | Low |
| MMR | Diverse docs | Better context | Medium |
| Multi Query | More coverage | Higher recall | Medium |
| Compression | Less noise | Efficient context | High |

---

## Installation

Install dependencies:

```bash
pip install langchain
pip install langchain-core
pip install langchain-community
pip install langchain-huggingface
pip install faiss-cpu
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

### Run MMR Retriever

```bash
python mmr.py
```

Example Output:

```
Result 1:
LangChain makes it easy to work with LLMs.

Result 2:
Embeddings are vector representations of text.

Result 3:
MMR helps you get diverse results...
```

---

## Modern LangChain Design

This project follows **modern LangChain retriever patterns**:

- VectorStoreRetriever
- MMR Retrieval Strategy
- Runnable-compatible retrievers

No deprecated chain-based retrievers used.

---

## Key Concepts Learned

### Retrieval Strategy

Strategy defines **how documents are selected**:

```
Query → Strategy → Documents
```

---

### Similarity Retrieval

```
Most Similar Documents
```

Fast but redundant.

---

### MMR Retrieval

```
Relevant + Diverse Documents
```

Better context for LLMs.

---

### Query Expansion

```
1 Query → Multiple Queries
```

Improves recall.

---

### Context Compression

```
Documents → Relevant Sections
```

Improves efficiency.

---

## Real World Applications

### MMR Retrieval

- RAG systems
- Research assistants
- Summarization systems
- Knowledge retrieval

---

### Multi Query Retrieval

- Search engines
- AI assistants
- Enterprise search
- Documentation search

---

### Contextual Compression

- Large documents
- Legal search
- Medical search
- Technical documentation

---

## Future Improvements

Possible extensions:

- Hybrid search (BM25 + embeddings)
- Re-ranking models
- Self-query retrievers
- Parent document retrievers
- LangGraph RAG pipelines
- Streaming retrieval
- Agentic retrieval

---

## Author

LangChain experimentation project focused on learning:

- Retrieval Strategies
- RAG Systems
- Vector Databases
- Modern LangChain Architecture

---

## Notes

Strategy-based retrieval is essential for building **high-quality production RAG systems**.

Simple similarity search works for small projects, but advanced retrieval strategies are required for **real-world AI applications.**