# LangChain Document Loaders

This module demonstrates how to load data from different sources using **LangChain Document Loaders.**

Document loaders are the **first step in most AI pipelines**, especially:

- Retrieval Augmented Generation (RAG)
- Semantic Search
- Question Answering Systems
- Document Analysis
- Knowledge Bases

This folder demonstrates how to load documents from:

- PDF files
- Text files
- CSV files
- Websites
- Directories
- Lazy loading streams

These examples use **LangChain Community Document Loaders**, which are the standard approach for document ingestion.

---

## Overview

Document loaders convert raw data into **LangChain Document objects.**

A Document object contains:

```
Document(
    page_content="Text content",
    metadata={"source": "..."}
)
```

These Document objects can then be used for:

- Text splitting
- Embeddings
- Vector databases
- RAG pipelines
- AI agents

---

## Folder Structure

```
document_loader/
│
├── csv_loader.py
├── directory_loader.py
├── lazy_loader.py
├── pdf_loader.py
├── text_loader.py
├── web_loader.py
│
├── test_document.pdf
├── proc&cons.txt
├── research-and-development-survey-2024-csv-notes.csv
│
├── befa_notes/
│   ├── BEFA Unit 1.pdf
│   ├── BEFA UNIT II.pdf
│   └── Unit III BE.pdf
│
└── README.md
```

---

## Document Object Structure

Every loader returns a list of Documents:

```python
docs = loader.load()
```

Example:

```
[
 Document(
  page_content="Some text...",
  metadata={"source": "file.pdf"}
 )
]
```

---

## 1. PDF Loader

File:

```
pdf_loader.py
```

Loads PDF documents using **PyPDFLoader**.

:contentReference[oaicite:0]{index=0}

---

### Code

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("test_document.pdf")

docs = loader.load()
```

---

### Output

```
7
Lorem ipsum dolor sit amet...
```

Each page of the PDF becomes a Document.

Example content is extracted from the test PDF. :contentReference[oaicite:1]{index=1}

---

### Use Cases

- Research papers
- Books
- Reports
- Notes
- Documentation

---

## 2. Text Loader

File:

```
text_loader.py
```

Loads plain text documents.

:contentReference[oaicite:2]{index=2}

---

### Code

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader(
    "proc&cons.txt",
    encoding="utf-8"
)

docs = loader.load()
```

---

### Output

Returns:

```
Document(
 page_content="Pros of AI...",
 metadata={...}
)
```

Example text includes AI advantages and disadvantages. :contentReference[oaicite:3]{index=3}

---

### Use Cases

- Notes
- Logs
- Articles
- Knowledge bases
- Transcripts

---

## 3. CSV Loader

File:

```
csv_loader.py
```

Loads structured data from CSV files.

:contentReference[oaicite:4]{index=4}

---

### Code

```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
 file_path="research-and-development-survey-2024-csv-notes.csv"
)

docs = loader.load()
```

---

### Output

Each row becomes a Document.

```
Row 1 → Document
Row 2 → Document
Row 3 → Document
```

---

### Use Cases

- Survey results
- Datasets
- Tables
- Structured records

---

## 4. Directory Loader

File:

```
directory_loader.py
```

Loads multiple documents from a directory.

:contentReference[oaicite:5]{index=5}

---

### Code

```python
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

loader = DirectoryLoader(
    path="befa_notes",
    loader_cls=PyPDFLoader,
    glob="*.pdf"
)

docs = loader.load()
```

---

### Output

Loads multiple PDF files including:

- BEFA Unit 1
- BEFA Unit II
- Unit III

Example content includes business economics topics like business structures and GDP. :contentReference[oaicite:6]{index=6}

---

### Use Cases

- Large document collections
- Knowledge bases
- Research archives
- Course notes

---

## 5. Lazy Loader

File:

```
lazy_loader.py
```

Loads documents **one at a time** instead of loading everything into memory.

:contentReference[oaicite:7]{index=7}

---

### Code

```python
docs = loader.lazy_load()

for doc in docs:
    print(doc.metadata)
```

---

### Difference from Normal Loading

Normal loading:

```
docs = loader.load()
```

Loads everything into memory.

Lazy loading:

```
docs = loader.lazy_load()
```

Loads documents one-by-one.

---

### Advantages

- Lower memory usage
- Better for large datasets
- Faster startup

---

### Use Cases

- Large document collections
- Big datasets
- Production pipelines

---

## 6. Web Loader

File:

```
web_loader.py
```

Loads content directly from websites.

:contentReference[oaicite:8]{index=8}

---

### Code

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
 "https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/"
)

docs = loader.load()
```

---

### Output

```
Full webpage content as text
```

---

### Use Cases

- Web scraping
- Knowledge extraction
- Documentation ingestion
- AI research assistants

---

## Load vs Lazy Load

| Feature | load() | lazy_load() |
|--------|--------|-------------|
| Memory Usage | High | Low |
| Speed | Slower startup | Faster startup |
| Dataset Size | Small-Medium | Large |
| Use Case | Prototyping | Production |

---

## Technologies Used

| Technology | Purpose |
|----------|---------|
| LangChain Community | Document Loaders |
| PyPDFLoader | PDF Extraction |
| CSVLoader | CSV Processing |
| TextLoader | Text Files |
| WebBaseLoader | Web Content |

---

## Installation

### 1 Install Dependencies

```bash
pip install langchain
pip install langchain-community
pip install pypdf
pip install beautifulsoup4
pip install requests
```

---

## Usage

### Load PDF

```
python pdf_loader.py
```

---

### Load Text File

```
python text_loader.py
```

---

### Load CSV

```
python csv_loader.py
```

---

### Load Directory

```
python directory_loader.py
```

---

### Lazy Loading

```
python lazy_loader.py
```

---

### Load Website

```
python web_loader.py
```

---

## Document Loading Pipeline

Typical RAG pipeline:

```
Documents
   ↓
Document Loaders
   ↓
Text Splitters
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retriever
   ↓
LLM
```

This folder implements the **Document Loaders stage**.

---

## Key Concepts Learned

### Document Objects

LangChain standard format:

```python
Document(
 page_content="text",
 metadata={}
)
```

---

### Metadata

Metadata example:

```
{
 "source": "file.pdf",
 "page": 1
}
```

Used for:

- Source tracking
- Citations
- Filtering

---

### Multi-Source Loading

LangChain allows combining sources:

- PDFs
- Websites
- CSV
- Text files

---

## Modern LangChain Design

This project uses modern LangChain components:

- langchain_community loaders
- Document objects
- Metadata support

No deprecated loaders used.

---

## Real World Applications

### RAG Systems

- Load documents
- Embed documents
- Query documents

---

### AI Assistants

- Knowledge bases
- Documentation bots

---

### Search Engines

- Semantic search
- Retrieval systems

---

### Data Analysis

- Structured datasets
- Reports

---

## Future Improvements

Possible extensions:

- JSON Loader
- Markdown Loader
- Notion Loader
- Google Docs Loader
- Database Loader
- API Loader

---

## Author

LangChain experimentation project focused on learning:

- Document Loaders
- Chat Models
- Chains
- Agents
- RAG
- LLM Architecture

---

## Notes

Document Loaders are the **entry point of all RAG systems.**

Understanding loaders is essential before learning:

- Text Splitters
- Embeddings
- Vector Databases
- Retrieval Systems