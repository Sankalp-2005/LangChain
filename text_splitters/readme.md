# LangChain Text Splitters

This module demonstrates **Text Splitting techniques in LangChain**, one of the most important preprocessing steps in **Retrieval-Augmented Generation (RAG)** systems.

Large documents cannot be directly fed into Large Language Models due to context limits.  
Text splitters divide documents into **manageable chunks** for embeddings and retrieval.

This folder covers three major types of text splitters:

- Length-Based Splitters
- Semantic Meaning-Based Splitters
- Structure-Based Splitters

These approaches represent the **core 20% of text splitting techniques used in real-world LLM applications.**

---

## Overview

Large documents must be split before:

- Embedding
- Indexing
- Retrieval
- RAG pipelines

Basic pipeline:

```
Document
   ↓
Text Splitter
   ↓
Chunks
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retriever
```

Good chunking improves:

- Retrieval accuracy
- Context quality
- LLM responses

Poor chunking causes:

- Lost context
- Irrelevant results
- Hallucinations

---

## Folder Structure

```
text_splitters/
│
├── char_text_splitter.py
├── pdf_char_text_splitter.py
├── recursive_splitter.py
├── semantic_chunker.py
├── code_splitter.py
├── test_document.pdf
│
└── README.md
```

---

## Types of Text Splitters

| Type | Method | Example |
|------|-------|---------|
| Length-Based | Fixed chunk size | CharacterTextSplitter |
| Semantic-Based | Meaning boundaries | SemanticChunker |
| Structure-Based | Document structure | Recursive Splitter |

---

# 1. Length-Based Splitters

Length-based splitters divide text using **fixed chunk sizes**.

They are:

- Fast
- Simple
- Predictable

But may break sentences or ideas.

---

## Character Text Splitter

File:

```
char_text_splitter.py
```

Uses `CharacterTextSplitter` to split text into fixed-size chunks. :contentReference[oaicite:0]{index=0}

---

### Implementation

```python
splitter = CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=0,
    is_separator_regex=False
)
```

---

### Parameters

| Parameter | Meaning |
|----------|---------|
| separator | Character used for splitting |
| chunk_size | Maximum chunk size |
| chunk_overlap | Overlapping characters |

---

### Example Flow

```
Large Text
   ↓
Character Splitter
   ↓
Chunks of 100 characters
```

---

## PDF Character Splitter

File:

```
pdf_char_text_splitter.py
```

Splits documents loaded from a PDF file. :contentReference[oaicite:1]{index=1}

Uses:

```
PyPDFLoader
```

to extract text from:

```
test_document.pdf
```

---

### Implementation

```python
loader = PyPDFLoader("test_document.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=500
)

result = splitter.split_documents(docs)
```

---

### Example Document

```
test_document.pdf
```

Contains multiple pages of text used for splitting. :contentReference[oaicite:2]{index=2}

---

## Advantages

- Fast
- Simple
- Easy to configure

---

## Limitations

- Breaks sentences
- Breaks ideas
- Lower retrieval quality

---

# 2. Semantic Meaning-Based Splitters

Semantic splitters divide text based on **meaning instead of length**.

Instead of splitting every N characters:

```
100 characters → split
```

They split when **topic or meaning changes**.

---

## Semantic Chunker

File:

```
semantic_chunker.py
```

Uses embeddings to detect **semantic boundaries**. :contentReference[oaicite:3]{index=3}

---

## Architecture

```
Text
   ↓
Embeddings
   ↓
Similarity Comparison
   ↓
Breakpoints
   ↓
Chunks
```

---

## Implementation

```python
splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)
```

---

## Embeddings Model

```python
HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2"
)
```

---

## Example Flow

```
Farming paragraph
   ↓
Chunk 1

Cricket paragraph
   ↓
Chunk 2

Terrorism paragraph
   ↓
Chunk 3
```

SemanticChunker detects topic changes automatically. :contentReference[oaicite:4]{index=4}

---

## Advantages

- Better context quality
- Natural chunk boundaries
- Higher retrieval accuracy

---

## Limitations

- Slower than length-based splitting
- Requires embeddings
- More computation

---

# 3. Structure-Based Splitters

Structure-based splitters use **document structure**.

They try to preserve:

- Paragraphs
- Sections
- Code blocks
- Sentences

Best for:

- Code
- Technical documents
- Books
- Articles

---

## Recursive Character Splitter

File:

```
recursive_splitter.py
```

Splits text hierarchically. :contentReference[oaicite:5]{index=5}

Order of splitting:

```
Paragraph
↓
Sentence
↓
Word
↓
Character
```

---

## Implementation

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)
```

---

## Example Flow

```
Paragraph
 ↓
Sentence groups
 ↓
Chunks
```

Recursive splitting preserves context better than basic splitting.

---

## Code Splitter

File:

```
code_splitter.py
```

Splits code while preserving programming structure. :contentReference[oaicite:6]{index=6}

---

## Implementation

```python
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300
)
```

---

## Example Flow

```
Python File
 ↓
Functions
 ↓
Chunks
```

Preserves:

- Functions
- Classes
- Logic blocks

---

## Advantages

- Preserves structure
- Better context
- Ideal for RAG

---

## Limitations

- Slightly slower
- More complex

---

# Comparison

| Type | Speed | Quality | Best Use Case |
|------|------|---------|--------------|
| Character Splitter | Fast | Low | Simple documents |
| Recursive Splitter | Medium | High | Most RAG systems |
| Semantic Splitter | Slow | Highest | Advanced RAG |

---

# Installation

Install dependencies:

```bash
pip install langchain
pip install langchain-core
pip install langchain-community
pip install langchain-text-splitters
pip install langchain-experimental
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

## Character Splitter

```
python char_text_splitter.py
```

---

## PDF Splitter

```
python pdf_char_text_splitter.py
```

---

## Recursive Splitter

```
python recursive_splitter.py
```

---

## Code Splitter

```
python code_splitter.py
```

---

## Semantic Splitter

```
python semantic_chunker.py
```

---

# Modern LangChain Design

This project uses modern LangChain components:

- CharacterTextSplitter
- RecursiveCharacterTextSplitter
- SemanticChunker
- PyPDFLoader

No deprecated splitters used.

---

# Key Concepts Learned

## Chunking

```
Large Document → Smaller Chunks
```

---

## Chunk Size

Defines:

```
Maximum tokens per chunk
```

---

## Chunk Overlap

Prevents context loss:

```
Chunk A: ABCDEFGHIJ
Chunk B: HIJKLMNOP
```

---

## Semantic Chunking

```
Meaning-based splitting
```

Better for RAG systems.

---

## Structure-Aware Chunking

```
Document structure preserved
```

Best for:

- Code
- Technical documents

---

# Real World Applications

Text splitters are used in:

- RAG systems
- Document search
- Chatbots
- Knowledge bases
- AI assistants
- Code search engines

---

# Best Practices

Recommended settings for RAG:

```
chunk_size = 500–1000
chunk_overlap = 50–150
```

Recommended splitter:

```
RecursiveCharacterTextSplitter
```

---

# Future Improvements

Possible extensions:

- Token-based splitters
- Markdown splitters
- HTML splitters
- Parent document splitters
- Sliding window chunking
- Adaptive chunking

---

# Author

LangChain experimentation project focused on learning:

- Text Splitting
- RAG Systems
- Document Processing
- Modern LangChain Architecture

---

# Notes

Text splitting is one of the most important steps in building **high-quality Retrieval-Augmented Generation (RAG) systems**.

Better chunking leads to **better retrieval and better LLM responses.**