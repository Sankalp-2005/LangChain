# LangChain Output Parsers

This module demonstrates how to use **Output Parsers in LangChain** to convert raw LLM responses into structured and usable formats.

Output parsers are essential for building reliable AI systems because they transform unstructured model outputs into:

- Clean text
- JSON objects
- Typed Python objects

This module covers:

- String Output Parsing
- JSON Output Parsing
- Pydantic Output Parsing

Output parsers are critical components for:

- AI agents
- Structured workflows
- Automation pipelines
- APIs powered by LLMs
- Data extraction systems

---

## Overview

LLMs normally return **unstructured text**:

```
The director of Titanic is James Cameron.
The main actors are Leonardo DiCaprio and Kate Winslet.
```

Output parsers convert this into structured data:

```json
{
 "director": ["James Cameron"],
 "actors": ["Leonardo DiCaprio","Kate Winslet"]
}
```

Structured outputs allow:

- Reliable automation
- API integration
- Data storage
- Validation
- Decision logic

---

## Folder Structure

```
output_parsers/
│
├── str_parser.py
├── json_parser.py
├── pydantic_parser.py
│
└── README.md
```

---

## Output Parser Types

| Parser | Output Type | Use Case |
|-------|-------------|----------|
| StrOutputParser | String | Text workflows |
| JsonOutputParser | Dictionary | Structured extraction |
| PydanticOutputParser | Python Object | Strong validation |

---

## 1. String Output Parser

File:

```
str_parser.py
```

Converts model output into plain text.

:contentReference[oaicite:0]{index=0}

---

### Architecture

```
Input
 ↓
Prompt
 ↓
LLM
 ↓
StrOutputParser
 ↓
Clean Text
```

---

### Code

```python
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
```

---

### Purpose

Ensures the output is returned as a clean string.

Without parser:

```
AIMessage(content="Text")
```

With parser:

```
"Text"
```

---

### Use Cases

- Text pipelines
- Summarization
- Research assistants
- Sequential chains

---

## 2. JSON Output Parser

File:

```
json_parser.py
```

Parses LLM responses into JSON objects.

:contentReference[oaicite:1]{index=1}

---

### Architecture

```
Movie Name
   ↓
PromptTemplate
   ↓
LLM
   ↓
JsonOutputParser
   ↓
Python Dictionary
```

---

### Code

```python
parser = JsonOutputParser()

template = PromptTemplate(
 template="Give me director, producer, actors:\n{movie}\n{format_instruction}",
 partial_variables={
  "format_instruction": parser.get_format_instructions()
 }
)

chain = template | model | parser
```

---

### Output

Example:

```python
{
 "director": ["James Cameron"],
 "producer": ["Jon Landau"],
 "actors": [
  "Leonardo DiCaprio",
  "Kate Winslet"
 ]
}
```

---

### Key Feature

Format instructions:

```python
parser.get_format_instructions()
```

This tells the LLM exactly how to structure output.

---

### Use Cases

- Data extraction
- APIs
- Automation
- Knowledge graphs
- Databases

---

## 3. Pydantic Output Parser

File:

```
pydantic_parser.py
```

Parses output into **typed Python objects with validation.**

:contentReference[oaicite:2]{index=2}

---

### Architecture

```
Movie Name
   ↓
PromptTemplate
   ↓
LLM
   ↓
Pydantic Parser
   ↓
Python Object
```

---

### Pydantic Model

```python
class Movie(BaseModel):
    Dicrector: list[str]
    Actor: list[str]
    Producer: list[str]
```

---

### Code

```python
parser = PydanticOutputParser(
 pydantic_object=Movie
)

chain = template | model | parser
```

---

### Output

Example:

```python
Movie(
 Director=["James Cameron"],
 Actor=["Leonardo DiCaprio"],
 Producer=["Jon Landau"]
)
```

---

### Advantages

- Strong typing
- Validation
- Reliable structure
- Production ready

---

## Parser Comparison

| Feature | String | JSON | Pydantic |
|--------|--------|------|---------|
| Structure | None | Medium | Strong |
| Validation | No | No | Yes |
| Python Objects | No | Dict | Class |
| Reliability | Low | Medium | High |
| Production Use | Limited | Good | Best |

---

## Technologies Used

| Technology | Purpose |
|----------|---------|
| LangChain Core | Output Parsers |
| HuggingFace Endpoint | LLM Access |
| PromptTemplate | Structured Prompts |
| Pydantic | Data Validation |

---

## Installation

### Install Dependencies

```bash
pip install langchain
pip install langchain-core
pip install langchain-huggingface
pip install pydantic
pip install python-dotenv
```

---

## Usage

### Run String Parser

```
python str_parser.py
```

---

### Run JSON Parser

```
python json_parser.py
```

---

### Run Pydantic Parser

```
python pydantic_parser.py
```

---

## How Output Parsers Work

Standard LLM call:

```
Prompt → Model → Text
```

With parsers:

```
Prompt → Model → Parser → Structured Output
```

---

## Runnable Integration

Output parsers integrate directly into chains:

```python
chain = prompt | model | parser
```

This is the modern LangChain pattern.

---

## Format Instructions

Output parsers provide instructions to the LLM:

```python
parser.get_format_instructions()
```

Example instruction:

```
Return output as valid JSON with fields:
director, actor, producer
```

This improves reliability.

---

## Modern LangChain Design

This project uses:

- Runnable chains
- PromptTemplate
- Output Parsers
- Structured outputs

No deprecated components used.

---

## Real World Applications

### AI Agents

Agents depend heavily on structured outputs:

```
Model → Parser → Tool Input
```

---

### APIs

LLM → JSON → API Response

---

### Automation

LLM → Structured Data → Database

---

### RAG Systems

LLM → Structured Answers → UI

---

## Key Concepts Learned

### Structured Outputs

LLMs become predictable when structured outputs are used.

---

### Runnable Parsers

Parsers integrate directly into pipelines:

```python
prompt | model | parser
```

---

### Reliability

Output parsers reduce hallucinations and formatting errors.

---

## Future Improvements

Possible extensions:

- XML Output Parser
- Regex Parser
- Custom Parsers
- Guardrails
- JSON Schema validation
- Structured streaming

---

## Author

LangChain experimentation project focused on learning:

- Chat Models
- Chains
- Agents
- Output Parsers
- Document Loaders
- RAG
- LLM Architecture

---

## Notes

Output parsers are essential for building **reliable AI applications.**

They transform LLMs from **text generators into structured data systems.**