# LangChain ChatModels & Embeddings

This module demonstrates how to work with **Chat Models and Embeddings in LangChain using HuggingFace endpoints.**

It covers the fundamental components required for building modern AI applications:

- Chat Models (LLM interaction)
- Embedding Models (Vector representations)

These components form the foundation for:

- Chatbots
- Agents
- RAG systems
- Search engines
- Semantic retrieval
- AI pipelines

This module represents the **core building blocks of any LangChain-based AI system.**

---

## Overview

Modern AI applications rely on two primary components:

### 1. Chat Models

Chat models generate natural language responses.

They are used for:

- Question answering
- Conversations
- Summarization
- Reasoning
- Code generation

---

### 2. Embeddings

Embeddings convert text into **numerical vectors**.

They are used for:

- Semantic search
- Similarity comparison
- Retrieval Augmented Generation (RAG)
- Clustering
- Recommendation systems

---

## Folder Structure

```
chatmodels/
│
├── chatmodel.py
├── embedding.py
│
└── README.md
```

---

## 1. chatmodel.py

Implements a **basic Chat Model invocation using LangChain.**

:contentReference[oaicite:0]{index=0}

This example demonstrates the simplest way to interact with an LLM through LangChain.

---

### Architecture

```
User Input
   ↓
ChatHuggingFace
   ↓
HuggingFace Endpoint
   ↓
LLM Response
   ↓
Console Output
```

---

### Key Code

```python
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke(input())
```

---

### How It Works

1. User enters text input
2. Input is sent to HuggingFace Endpoint
3. Model generates response
4. Response is printed

---

### Execution

```bash
python chatmodel.py
```

---

### Example

Input:

```
Explain artificial intelligence
```

Output:

```
Artificial Intelligence is a branch of computer science focused on building systems that can perform tasks requiring human intelligence.
```

---

### Concepts Demonstrated

- Chat Models
- Model Invocation
- HuggingFaceEndpoint
- LangChain Chat Interface

---

## 2. embedding.py

Implements **text embeddings using HuggingFace embedding models.**

:contentReference[oaicite:1]{index=1}

This example demonstrates how to convert text into vector representations.

---

### Architecture

```
Text Input
   ↓
Embedding Model
   ↓
Vector Representation
   ↓
Console Output
```

---

### Key Code

```python
embedding = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2"
)

vector = embedding.embed_query("Hello World")
```

---

### Output

Example Output:

```
384
[0.0213, -0.1142, 0.4431, ...]
```

Where:

- **384** = vector dimension
- Each number = semantic feature

---

### Concepts Demonstrated

- Embedding Models
- Vector Representations
- Semantic Encoding
- HuggingFace Embeddings

---

## Chat Models vs Embeddings

| Feature | Chat Models | Embeddings |
|---------|-------------|------------|
| Output | Text | Vector |
| Purpose | Generation | Representation |
| Example Task | Chatbot | Semantic Search |
| Input | Prompt | Text |
| Output Type | Natural Language | Float Array |

---

## Technologies Used

| Technology | Purpose |
|----------|---------|
| LangChain Core | Model Interfaces |
| HuggingFace Endpoint | Model Access |
| ChatHuggingFace | Chat Interface |
| HuggingFace Embeddings | Vector Encoding |
| Python Dotenv | Environment Variables |

---

## Installation

### 1. Clone Repository

```bash
git clone <your_repo_url>
cd langchain-project
```

---

### 2. Install Dependencies

```bash
pip install langchain
pip install langchain-core
pip install langchain-huggingface
pip install python-dotenv
```

---

### 3. Setup Environment Variables

Create a `.env` file:

```
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
```

---

## Usage

### Run Chat Model

```
python chatmodel.py
```

Example:

```
Explain neural networks
```

---

### Run Embedding Model

```
python embedding.py
```

Example Output:

```
384
[0.0213, -0.1142, 0.4431 ...]
```

---

## How Chat Models Work

Chat models generate responses based on input prompts.

Example:

```
Prompt → Model → Response
```

LangChain Invocation:

```python
model.invoke("Hello")
```

---

## How Embeddings Work

Embeddings convert text into vectors.

Example:

```
"Cat" → [0.12, -0.44, 0.92, ...]
"Dog" → [0.10, -0.40, 0.89, ...]
```

Similar meanings → similar vectors.

Distance measures similarity:

- Cosine similarity
- Euclidean distance
- Dot product

---

## Vector Dimensions

Embedding models produce fixed-size vectors.

Example:

```
all-MiniLM-L6-v2 → 384 dimensions
```

Higher dimensions:

- Better semantic accuracy
- Higher computation cost

---

## Modern LangChain Design

This project uses **modern LangChain architecture:**

- Chat Models
- Embedding Models
- HuggingFace Endpoints
- Runnable-based invocation

No deprecated components like:

- OpenAIEmbeddings (legacy usage)
- LLMChain-based calls

---

## Real World Applications

### Chat Models

Used in:

- AI assistants
- Agents
- Chatbots
- Document analysis
- Code generation

---

### Embeddings

Used in:

- RAG systems
- Vector databases
- Semantic search
- Recommendations
- Clustering
- Similarity detection

---

## Key Concepts Learned

### Chat Model Invocation

```python
model.invoke(prompt)
```

Returns:

```
AIMessage
```

Access text with:

```python
result.content
```

---

### Embedding Generation

```python
embedding.embed_query(text)
```

Returns:

```
List[float]
```

---

### HuggingFaceEndpoint

Provides:

- Hosted models
- API access
- Scalable inference

---

## Models Used

### Chat Model

```
openai/gpt-oss-20b
```

Accessed via:

```
HuggingFaceEndpoint
```

---

### Embedding Model

```
sentence-transformers/all-MiniLM-L6-v2
```

Accessed via:

```
HuggingFaceEndpointEmbeddings
```

---

## Future Improvements

Possible extensions:

- Streaming chat models
- Async model calls
- Batch embeddings
- Vector database integration
- RAG pipelines
- Evaluation pipelines
- Multi-model comparison

---

## Author

LangChain experimentation project focused on learning:

- Modern LangChain
- Chains
- Agents
- Tools
- Chat Models
- Embeddings
- LLM Architecture

---

## Notes

This module provides the **fundamental building blocks required before learning chains, agents, and RAG.**

Understanding chat models and embeddings is essential for building **production-grade AI applications.**