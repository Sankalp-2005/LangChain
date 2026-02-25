# LangChain Prompts

This module demonstrates how to create, save, load, and use **Prompt Templates in LangChain.**

Prompts are one of the most important components in any LLM-based application.  
Well-designed prompts determine the quality, structure, and reliability of model outputs.

This module covers:

- PromptTemplate creation
- Template validation
- Saving prompts to files
- Loading prompts from files
- Using prompts in applications
- Prompt-based UI with Streamlit

These examples follow **modern LangChain prompt design practices.**

---

## Overview

A **Prompt Template** allows dynamic generation of prompts using variables.

Instead of writing static prompts:

```
Summarize Artificial Intelligence
```

We create reusable templates:

```
Summarize {topic}
```

Then provide values dynamically:

```
topic = "Artificial Intelligence"
```

Final Prompt:

```
Summarize Artificial Intelligence
```

Prompt templates make AI systems:

- Reusable
- Scalable
- Maintainable
- Structured

---

## Folder Structure

```
prompts/
│
├── prompt.py
├── prompt_ui.py
├── template.json
│
└── README.md
```

---

## PromptTemplate Basics

Prompt templates are created using:

```python
from langchain_core.prompts import PromptTemplate
```

Example template:

```
You are an agent whose job is to provide summaries on the topic {topic}
```

The variable:

```
{topic}
```

is replaced dynamically.

---

## 1. Creating a Prompt Template

File:

```
prompt.py
```

Creates and saves a PromptTemplate.

:contentReference[oaicite:0]{index=0}

---

### Code

```python
template = PromptTemplate(
 template="""
 You are an agent who job is to provided summaries on the topic {topic}
 """,
 input_variables=["topic"],
 validate_template=True
)

template.save("template.json")
```

---

### Features

- Template validation
- Variable definition
- JSON export

---

### Template Validation

```
validate_template=True
```

Ensures:

- Variables exist
- Syntax is correct
- Template is valid

Prevents runtime errors.

---

## 2. Saved Prompt Template

File:

```
template.json
```

:contentReference[oaicite:1]{index=1}

---

### Example

```json
{
 "input_variables": ["topic"],
 "template": "You are an agent who job is to provided summaries on the topic {topic}",
 "template_format": "f-string"
}
```

---

### Advantages

Saved prompts allow:

- Version control
- Reuse
- Prompt management
- Production deployment

---

## 3. Loading Prompts

File:

```
prompt_ui.py
```

Loads a saved prompt template.

:contentReference[oaicite:2]{index=2}

---

### Code

```python
from langchain_core.prompts import load_prompt

template = load_prompt("template.json")
```

---

### Advantages

Separates:

```
Prompt Logic
```

from:

```
Application Code
```

This is a production design pattern.

---

## 4. Prompt + Model Chain

Prompts integrate directly with models:

```python
chain = template | model
```

Example invocation:

```python
result = chain.invoke({
 "topic": "Artificial Intelligence"
})
```

---

## 5. Streamlit Prompt UI

File:

```
prompt_ui.py
```

Implements a simple UI for prompt interaction.

:contentReference[oaicite:3]{index=3}

---

### Architecture

```
User Input
   ↓
Streamlit UI
   ↓
Prompt Template
   ↓
LLM
   ↓
Output
```

---

### Code Structure

```python
st.header("Research Tool")

user_input = st.text_input("Enter topic")

if st.button("Send"):
    result = chain.invoke({
        "topic": user_input
    })
```

---

### Features

- Interactive UI
- Dynamic prompts
- Live LLM responses
- Prompt reuse

---

## Technologies Used

| Technology | Purpose |
|----------|---------|
| LangChain Core | Prompt Templates |
| HuggingFace Endpoint | LLM Access |
| Streamlit | UI Interface |
| JSON | Prompt Storage |

---

## Installation

### Install Dependencies

```bash
pip install langchain
pip install langchain-core
pip install langchain-huggingface
pip install streamlit
pip install python-dotenv
```

---

## Usage

### Create Prompt Template

```
python prompt.py
```

Creates:

```
template.json
```

---

### Run Prompt UI

```
streamlit run prompt_ui.py
```

---

## Prompt Lifecycle

Typical workflow:

```
Design Prompt
   ↓
Create Template
   ↓
Save Template
   ↓
Load Template
   ↓
Use with Model
```

This project demonstrates the full lifecycle.

---

## Prompt Variables

Variables are defined:

```python
input_variables=["topic"]
```

Used in template:

```
{topic}
```

Passed at runtime:

```python
chain.invoke({
 "topic": "Machine Learning"
})
```

---

## Modern LangChain Design

This project uses modern LangChain prompt architecture:

- PromptTemplate
- load_prompt()
- Runnable Chains
- JSON prompt storage

No deprecated prompt formats used.

---

## Best Practices Demonstrated

### 1. Template Validation

```
validate_template=True
```

Ensures reliability.

---

### 2. Prompt Separation

```
template.json
```

keeps prompts separate from code.

---

### 3. Reusable Prompts

One template → multiple uses.

---

### 4. Runnable Chains

```
template | model
```

Modern LangChain pattern.

---

## Real World Applications

### AI Assistants

Reusable prompts for:

- Research
- Coding
- Writing

---

### RAG Systems

Prompt templates for:

- Retrieval prompts
- Context injection

---

### Agents

Prompt templates define:

- Agent behavior
- Instructions

---

### Production Systems

Stored prompts allow:

- Versioning
- Updates
- Testing

---

## Key Concepts Learned

### Prompt Templates

Dynamic prompts:

```
Template + Variables → Prompt
```

---

### Prompt Storage

Templates saved as:

```
JSON
```

---

### Prompt Loading

Reusable prompt architecture.

---

### Prompt Chains

```
Prompt → Model → Output
```

---

## Future Improvements

Possible extensions:

- ChatPromptTemplate
- Few-shot prompts
- System prompts
- Prompt evaluation
- Prompt versioning
- Prompt optimization

---

## Author

LangChain experimentation project focused on learning:

- Prompts
- Chat Models
- Chains
- Agents
- RAG
- LLM Architecture

---

## Notes

Prompt engineering is one of the most important skills in building AI systems.

Well-designed prompts improve:

- Accuracy
- Reliability
- Consistency

This module demonstrates the **core prompt workflow used in real AI applications.**