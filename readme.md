# LangChain Engineering Repository

This repository is a **structured deep-dive into modern LangChain development**, covering the core components required to build **production-grade LLM applications and AI Agents.**

The goal of this project is to systematically learn and implement the **fundamental building blocks of LangChain**, including:

- Chat Models
- Prompts
- Output Parsers
- Document Loaders
- Text Splitters
- Embeddings
- Vector Stores
- Retrievers
- Chains
- Tools
- Tool Calling
- RAG Pipelines
- Structured Outputs

This repository focuses on **modern LangChain architecture (Runnable-based)** instead of deprecated components.

---

# Repository Overview

This project is organized into **modular topics**, each representing a major component of LangChain.

```
langchain/
│
├── chatmodels/
├── prompts/
├── chatbots/
├── output_parsers/
├── document_loader/
│
├── runnables/
├── chains/
├── tools/
├── tool_calling/
│
├── text_splitters/
├── vector_stores/
├── retrievers_source_based/
├── retrievers_strategy_based/
│
├── structured_output/
├── rag/
│
└── README.md
```

Each folder contains:

- Working code examples
- Focused implementations
- Practical demonstrations
- Detailed documentation

---

# Learning Path

This repository follows a logical progression from **basic LLM interaction → advanced AI systems**.

```
Chat Models
   ↓
Prompts
   ↓
Output Parsers
   ↓
Chatbots
   ↓
Document Loaders
   ↓
Text Splitters
   ↓
Embeddings
   ↓
Vector Stores
   ↓
Retrievers
   ↓
Chains
   ↓
Tools
   ↓
Tool Calling
   ↓
Structured Output
   ↓
RAG
   ↓
Agents (Future)
```

---

# Modules

---

## 1. Chat Models

Folder:

```
chatmodels/
```

Chat Models provide the **core interface for interacting with LLMs.**

Covered components:

- ChatHuggingFace
- HuggingFaceEndpoint
- Embedding Models

Concepts learned:

- Model invocation
- Chat interfaces
- Embeddings
- Vector representations

Example:

```
User Input → Model → Response
```

Embeddings:

```
Text → Vector Representation
```

Embeddings are used for:

- Vector search
- Retrieval
- RAG pipelines

---

## 2. Prompts

Folder:

```
prompts/
```

Prompts define how LLMs behave.

Covered components:

- PromptTemplate
- Template validation
- Prompt saving
- Prompt loading
- Prompt-based UI

Concepts learned:

- Dynamic prompts
- Prompt variables
- Prompt reuse
- Prompt lifecycle

Example:

```
Template + Variables → Prompt
```

---

## 3. Output Parsers

Folder:

```
output_parsers/
```

Output parsers convert LLM responses into structured formats.

Covered parsers:

- StrOutputParser
- JsonOutputParser
- PydanticOutputParser

Concepts learned:

- Structured outputs
- JSON parsing
- Typed objects
- Data validation

Example:

```
LLM → Parser → Structured Output
```

---

## 4. Chatbots

Folder:

```
chatbots/
```

Chatbots maintain conversation state across multiple messages.

Covered topics:

- Message-based chat
- Chat history
- Session chatbots
- ChatPromptTemplate

Concepts learned:

- Stateful conversations
- Message objects
- Dynamic prompts
- Persistent sessions

Example:

```
User → Chat History → Model → Response
```

---

## 5. Document Loaders

Folder:

```
document_loader/
```

Document loaders convert raw data into LangChain Documents.

Covered loaders:

- PDF Loader
- Text Loader
- CSV Loader
- Directory Loader
- Lazy Loader
- Web Loader

Concepts learned:

- Document ingestion
- Metadata
- Multi-source loading
- Lazy loading

Example:

```
Documents → Document Objects
```

Document loaders are the **first step of RAG pipelines.**

---

## 6. Runnables

Folder:

```
runnables/
```

Runnables are the **core abstraction in modern LangChain**.

They replace legacy components such as:

- LLMChain
- SequentialChain
- RouterChain

Covered components:

- RunnableSequence
- RunnableParallel
- RunnableBranch
- RunnableLambda
- RunnablePassthrough

Concepts learned:

- Runnable composition
- Sequential execution
- Parallel execution
- Conditional pipelines
- Custom logic integration

Example pipeline:

```
Prompt → Model → Parser → Output
```

---

## 7. Chains

Folder:

```
chains/
```

Chains combine multiple LLM steps into workflows.

Covered chain types:

- Sequential Chains
- Parallel Chains
- Conditional Chains

Concepts learned:

- Multi-step reasoning
- Prompt chaining
- Structured workflows
- Branching logic

Example:

```
Topic → Research → Summary
```

---

## 8. Tools

Folder:

```
tools/
```

Tools allow LLMs to interact with external logic.

Covered methods:

- @tool decorator
- StructuredTool
- BaseTool
- Toolkits
- Built-in Tools

Concepts learned:

- Tool schemas
- Tool metadata
- Tool invocation
- Tool organization

Example:

```
LLM → Multiply Tool → Result
```

---

## 9. Tool Calling

Folder:

```
tool_calling/
```

Tool calling allows LLMs to dynamically execute tools.

Covered topics:

- Tool binding
- Tool calls
- Tool execution
- Injected arguments
- Multi-tool pipelines

Example:

```
User Query
   ↓
LLM
   ↓
Exchange Rate API
   ↓
Calculation Tool
   ↓
Final Answer
```

---

## 10. Text Splitters

Folder:

```
text_splitters/
```

Text splitters prepare documents for embeddings and retrieval.

Covered splitter types:

### Length-Based

- CharacterTextSplitter
- PDF splitting

### Semantic-Based

- SemanticChunker

### Structure-Based

- RecursiveCharacterTextSplitter
- Code splitters

Concepts learned:

- Chunk size tuning
- Chunk overlap
- Semantic boundaries
- Structure preservation

Example:

```
Document → Chunks → Embeddings
```

---

## 11. Vector Stores

Folder:

```
vector_stores/
```

Vector stores enable semantic search.

Implemented databases:

- Chroma Vector Store
- FAISS Vector Store

Operations covered:

- Add documents
- Similarity search
- Similarity scoring
- Metadata filtering
- Update documents
- Delete documents
- Persistent storage

Concepts learned:

- Embeddings
- Vector search
- Metadata filtering
- Persistence

Example:

```
Query → Embeddings → Vector Search → Documents
```

---

## 12. Retrievers

Folders:

```
retrievers_source_based/
retrievers_strategy_based/
```

Retrievers fetch relevant documents for LLMs.

### Source-Based Retrievers

- VectorStoreRetriever
- WikipediaRetriever

Concepts learned:

- Knowledge retrieval
- External data sources
- Similarity retrieval

---

### Strategy-Based Retrievers

- MMR Retrieval
- Multi Query Retrieval (conceptual)
- Contextual Compression (conceptual)

Concepts learned:

- Retrieval diversity
- Query expansion
- Context optimization

---

## 13. Structured Output

Folder:

```
structured_output/
```

Structured output ensures reliable LLM responses.

Covered approaches:

- JSON Schema
- Pydantic Models
- TypedDict

Concepts learned:

- Schema enforcement
- Data validation
- Reliable outputs

Example:

```
Text → Structured Data
```

---

## 14. Retrieval Augmented Generation (RAG)

Folder:

```
rag/
```

RAG combines retrieval and generation to produce accurate answers.

Covered pipeline:

- Transcript extraction
- Text splitting
- Embeddings
- Vector database
- Retrieval
- Prompting
- Answer generation

Concepts learned:

- Context injection
- Hallucination reduction
- Semantic retrieval
- Vector databases

Example:

```
Query → Retrieval → Context → LLM → Answer
```

This module demonstrates a **complete end-to-end RAG pipeline.**

---

# Technologies Used

| Technology | Purpose |
|----------|---------|
| LangChain Core | Runnable architecture |
| LangChain Community | Tools and integrations |
| LangChain Chroma | Vector database |
| LangChain Text Splitters | Document chunking |
| LangChain Google GenAI | Gemini models |
| LangChain HuggingFace | Embeddings & models |
| ChromaDB | Vector storage |
| FAISS | Vector indexing |
| Pydantic | Structured output |
| Streamlit | Prompt UI |
| Python Dotenv | Environment variables |

---

# Installation

Clone repository:

```
git clone <repo_url>
cd langchain
```

Install dependencies:

```
pip install langchain
pip install langchain-core
pip install langchain-community
pip install langchain-chroma
pip install langchain-huggingface
pip install langchain-google-genai
pip install langchain-text-splitters
pip install langchain-experimental
pip install chromadb
pip install faiss-cpu
pip install duckduckgo-search
pip install youtube-transcript-api
pip install pytube
pip install pydantic
pip install streamlit
pip install python-dotenv
pip install requests
```

---

# Environment Setup

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key
HUGGINGFACEHUB_API_TOKEN=your_api_key
Exchange_rate_api_key=your_api_key
```

---

# Modern LangChain Architecture

This repository uses **modern LangChain design (2025+)**

Key principles:

- Runnable-based workflows
- Structured outputs
- Tool binding
- Vector retrieval
- Schema validation
- Prompt templates
- Output parsers

No deprecated components used:

- LLMChain
- SimpleSequentialChain
- AgentExecutor chains

---

# Key Concepts Covered

This repository covers the **core building blocks required for production AI systems:**

### LLM Pipelines

```
Input → Prompt → Model → Output
```

### Retrieval Systems

```
Query → Retriever → Documents
```

### RAG Systems

```
Query → Retrieval → LLM → Answer
```

### Tool-Based Systems

```
LLM → Tools → Result
```

### Structured Systems

```
LLM → Schema → Validated Output
```

---

# Real World Applications

Concepts in this repository apply to:

- AI Assistants
- RAG Systems
- Enterprise Search
- Automation Agents
- Research Assistants
- Coding Assistants
- Knowledge Bases

---

# Future Work

Planned extensions:

- LangGraph Agents
- Memory Systems
- Multi-Agent Systems
- Evaluation Pipelines
- Streaming Applications

---

# Author

LangChain experimentation project focused on learning:

- Modern LangChain Architecture
- AI Agents
- Retrieval Systems
- Tool Calling
- Structured Outputs

---

# Notes

This repository is designed as a **systematic LangChain engineering reference** rather than a collection of random examples.

It focuses on the **essential 20% of LangChain that covers 80% of real-world AI development.**