# Retrieval Augmented Generation (RAG)

This module demonstrates how to build a **Retrieval Augmented Generation (RAG) pipeline using LangChain.**

RAG combines:

- Document Retrieval
- Embeddings
- Vector Databases
- LLM Reasoning

to produce **accurate, context-aware answers.**

This implementation builds a **YouTube Transcript Question-Answering System** that:

1. Extracts transcripts from a YouTube video  
2. Splits text into chunks  
3. Converts text into embeddings  
4. Stores vectors in FAISS  
5. Retrieves relevant chunks  
6. Uses an LLM to answer questions from context

This represents a **complete end-to-end RAG pipeline.**

---

## Overview

Large Language Models do not have access to private or external data.

RAG solves this problem by:

1. Retrieving relevant information
2. Providing context to the LLM
3. Generating grounded answers

Instead of:

```
User → LLM → Answer (may hallucinate)
```

RAG uses:

```
User → Retriever → Context → LLM → Answer
```

This produces:

- More accurate answers
- Fewer hallucinations
- Source-based responses

---

## File Structure

```
rag/
│
├── rag.py
│
└── README.md
```

---

## Architecture

```
YouTube URL
   ↓
Transcript Extraction
   ↓
Text Splitting
   ↓
Embeddings
   ↓
FAISS Vector Store
   ↓
Retriever
   ↓
Prompt Template
   ↓
LLM
   ↓
Answer
```

---

## RAG Pipeline Components

This implementation includes all major RAG components.

---

## 1. Transcript Extraction

The system extracts transcripts from a YouTube video.

:contentReference[oaicite:0]{index=0}

### Code

```python
video_id = YouTube(url).video_id

transcript_list = YouTubeTranscriptApi().fetch(video_id)

text = " ".join(chunk.text for chunk in transcript_list)
```

---

### Purpose

Converts video content into text that can be processed by the RAG pipeline.

---

### Advantages

- Real-time data ingestion
- Automatic knowledge extraction
- Flexible input sources

---

## 2. Text Splitting

Large texts must be split into smaller chunks before embedding.

:contentReference[oaicite:1]{index=1}

### Code

```python
splitter = RecursiveCharacterTextSplitter(
 chunk_size=1000,
 chunk_overlap=200
)

chunks = splitter.create_documents([text])
```

---

### Purpose

Prepares documents for embeddings.

---

### Why Splitting Is Required

LLMs and embedding models have token limits.

Splitting allows:

- Efficient retrieval
- Better semantic matching
- Faster search

---

## 3. Embeddings

Text chunks are converted into vectors.

:contentReference[oaicite:2]{index=2}

### Code

```python
embeddings = HuggingFaceEndpointEmbeddings(
 repo_id="BAAI/bge-m3"
)
```

---

### Purpose

Embeddings allow semantic search.

Example:

```
"Neural Networks"
≈
"Deep Learning"
```

Similar meaning → similar vectors.

---

## 4. Vector Store (FAISS)

Embeddings are stored in FAISS.

:contentReference[oaicite:3]{index=3}

### Code

```python
vector_store = FAISS.from_documents(
 chunks,
 embeddings
)
```

---

### Purpose

Allows fast similarity search.

---

### Why FAISS

- Fast vector search
- Local database
- No external services
- Ideal for prototypes

---

## 5. Retriever

Retriever finds relevant chunks.

:contentReference[oaicite:4]{index=4}

### Code

```python
retriever = vector_store.as_retriever(
 search_type="similarity",
 search_kwargs={"k":4}
)
```

---

### Purpose

Returns the most relevant document chunks.

```
Query → Top 4 Chunks
```

---

## 6. Context Formatter

Formats retrieved documents.

:contentReference[oaicite:5]{index=5}

### Code

```python
def output_formatter(docs):
 return "\n\n".join(
  doc.page_content
  for doc in docs
 )
```

---

### Purpose

Combines retrieved chunks into a single context string.

---

## 7. Parallel Chain

Builds context + query simultaneously.

:contentReference[oaicite:6]{index=6}

### Code

```python
parallel_chain = RunnableParallel(
 {
  "context": retriever | RunnableLambda(output_formatter),
  "query": RunnablePassthrough()
 }
)
```

---

### Purpose

Creates structured inputs:

```
{
 context: retrieved_text,
 query: user_query
}
```

---

## 8. Prompt Template

Defines how the LLM should answer.

:contentReference[oaicite:7]{index=7}

### Code

```python
template = PromptTemplate(
 template="""
 You are a helpful assistant
 answer only from the given context:{context}
 and respond to the query:{query}
 if you don't know say 'don't know'
 """,
 input_variables=["context","query"]
)
```

---

### Important Feature

```
answer only from the given context
```

Prevents hallucinations.

---

## 9. LLM Generation

Uses a HuggingFace LLM.

:contentReference[oaicite:8]{index=8}

### Code

```python
model = ChatHuggingFace(llm=llm)
```

---

### Model Used

```
meta-llama/Llama-4-Scout-17B-16E-Instruct
```

---

## 10. Final Chain

Full RAG pipeline.

:contentReference[oaicite:9]{index=9}

### Code

```python
main_chain = (
 parallel_chain
 | template
 | model
 | string_parser
)
```

---

## Execution

Run:

```
python rag.py
```

---

### Input

```
Enter the url:
https://youtube.com/....

User:
What is reinforcement learning?
```

---

### Output

```
Reinforcement learning is a method where an agent learns through rewards and penalties...
```

---

## Technologies Used

| Technology | Purpose |
|----------|---------|
| LangChain Core | Chains |
| FAISS | Vector Database |
| HuggingFace Embeddings | Vector Generation |
| HuggingFace LLM | Answer Generation |
| RecursiveTextSplitter | Document Chunking |
| YouTubeTranscriptAPI | Transcript Extraction |
| PyTube | Video Processing |

---

## Installation

### Install Dependencies

```bash
pip install langchain
pip install langchain-core
pip install langchain-huggingface
pip install langchain-text-splitters
pip install langchain-community
pip install faiss-cpu
pip install youtube-transcript-api
pip install pytube
pip install python-dotenv
```

---

## RAG Pipeline Explained

Standard pipeline:

```
Documents
   ↓
Text Splitter
   ↓
Embeddings
   ↓
Vector Store
   ↓
Retriever
   ↓
Prompt
   ↓
LLM
   ↓
Answer
```

This project implements the **complete pipeline.**

---

## Key Concepts Learned

### Embedding-Based Retrieval

Semantic search instead of keyword search.

---

### Vector Databases

Store embeddings for fast retrieval.

---

### Context Injection

LLM receives:

```
Context + Query
```

---

### Hallucination Reduction

RAG forces model to answer from:

```
Retrieved Context
```

---

## Modern LangChain Design

This project uses modern LangChain architecture:

- Runnable Chains
- FAISS VectorStore
- PromptTemplate
- HuggingFace Endpoints
- Output Parsers

No deprecated components used.

---

## Real World Applications

### Enterprise AI Assistants

- Internal documentation
- Knowledge bases

---

### Research Tools

- Paper search
- Video search

---

### Customer Support

- Product documentation
- FAQs

---

### AI Tutors

- Course material
- Lecture transcripts

---

## Future Improvements

Possible extensions:

- Persistent vector database
- Multi-document RAG
- Hybrid search
- Re-ranking
- Streaming responses
- Web UI
- LangGraph RAG

---

## Author

LangChain experimentation project focused on learning:

- Chat Models
- Chains
- Prompts
- Output Parsers
- Document Loaders
- RAG
- LLM Architecture

---

## Notes

RAG is one of the most important skills in modern AI engineering.

Understanding RAG enables building:

- Knowledge assistants
- AI search engines
- Enterprise AI systems