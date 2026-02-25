# LangChain Chains

This module demonstrates how to build **LLM Chains using modern LangChain Runnables**.  
It covers the three most important chain patterns used in real-world LLM systems:

- Sequential Chains
- Parallel Chains
- Conditional (Branching) Chains

The examples use **LangChain Runnable API** with **HuggingFace models**, which reflects the modern LangChain architecture (post-2024).

---

## Overview

Chains allow you to connect multiple LLM calls into structured workflows.

Instead of calling an LLM directly, chains enable:

- Multi-step reasoning
- Structured pipelines
- Data transformation
- Conditional execution
- Parallel processing

This folder demonstrates the **core 20% of LangChain Chains that covers 80% of real-world usage.**

---

## Architecture

Modern LangChain chains are built using **Runnable Composition**.

Example pattern:

```
Input → Prompt → Model → Parser → Next Step → Output
```

Example:

```
User Input
   ↓
PromptTemplate
   ↓
LLM
   ↓
OutputParser
   ↓
Next Prompt
   ↓
LLM
   ↓
Final Output
```

Chains are composed using the pipe operator:

```python
chain = step1 | step2 | step3
```

---

## Files

### 1. sequential_chain.py

Implements a **Sequential Chain** where the output of one LLM call becomes the input to another.

### Flow

```
Topic
  ↓
Research Agent Prompt
  ↓
LLM
  ↓
Raw Information
  ↓
Summary Prompt
  ↓
LLM
  ↓
Final Summary
```

### Purpose

Demonstrates:

- Multi-step reasoning
- Prompt chaining
- Output passing
- Runnable composition

### Key Code

```python
chain = template1 | model | parser | template2 | model | parser
```

### Use Cases

- Research → Summary pipelines
- Data extraction → Formatting
- Multi-stage reasoning
- Document processing pipelines

---

### 2. parallel_chain.py

Implements a **Parallel Chain** where multiple LLM calls execute simultaneously.

### Flow

```
Text
  ↓
 ┌─────────────┐
 │             │
Pros Chain     Cons Chain
 │             │
 └──────┬──────┘
        ↓
    Merge Prompt
        ↓
       LLM
        ↓
      Output
```

### Purpose

Demonstrates:

- Concurrent LLM calls
- Structured outputs
- Result merging
- RunnableParallel

### Key Code

```python
parallel_chain = RunnableParallel(
    {
        "pros": template_pros | model | parser,
        "cons": template_cons | model | parser
    }
)
```

### Use Cases

- Pros vs Cons analysis
- Multi-perspective reasoning
- Independent subtasks
- Structured generation

---

### 3. conditional_chain.py

Implements a **Conditional Chain (Branching Logic)** based on model output.

### Flow

```
Feedback
   ↓
Classifier Prompt
   ↓
LLM
   ↓
Pydantic Parser
   ↓
Sentiment Object
   ↓
RunnableBranch
   ↓
 ┌──────────────┐
 │              │
Positive Chain  Negative Chain
 │              │
 └──────┬───────┘
        ↓
      Output
```

### Purpose

Demonstrates:

- Structured output parsing
- Pydantic integration
- Conditional execution
- RunnableBranch

### Key Components

#### Structured Output Model

```python
class Sentiment(BaseModel):
    sentiment: Literal["positive","negative"]
```

#### Branch Logic

```python
branch_chain = RunnableBranch(
    (lambda x: x.sentiment=="positive", positive_chain),
    (lambda x: x.sentiment=="negative", negative_chain),
)
```

### Use Cases

- Chatbot routing
- Intent classification
- Decision systems
- AI workflows
- Tool routing
- Agent decision logic

---

## Technologies Used

| Technology | Purpose |
|----------|---------|
| LangChain Core | Runnable Chains |
| HuggingFace Endpoint | LLM Access |
| Pydantic | Structured Output |
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
pip install pydantic
```

---

### 3. Setup Environment Variables

Create a `.env` file:

```
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
```

---

## Usage

### Sequential Chain

```bash
python sequential_chain.py
```

Example Input:

```
Artificial Intelligence
```

Example Output:

```
Artificial Intelligence is a field of computer science...
(5 line summary)
```

---

### Parallel Chain

```bash
python parallel_chain.py
```

Example Output:

```
Pros:
- Automation
- Faster decisions
- Personalization

Cons:
- Job displacement
- Privacy risks
- High cost
```

---

### Conditional Chain

```bash
python conditional_chain.py
```

Example Input:

```
This is a wonderful phone
```

Example Output:

```
Thank you for your positive feedback!
We are glad you enjoyed the product.
```

---

## Runnable Graph Visualization

Each chain prints its execution graph:

```python
final_chain.get_graph().print_ascii()
```

Example:

```
Prompt → Model → Parser → Branch → Output
```

This helps visualize chain architecture.

---

## Key Concepts Learned

### Runnable API

Modern LangChain uses **Runnables instead of legacy Chains.**

Example:

```python
chain = prompt | model | parser
```

This replaces:

```
LLMChain (Deprecated)
SimpleSequentialChain (Deprecated)
```

---

### Sequential Execution

```
Step A → Step B → Step C
```

Used when:

- Later steps depend on earlier results

---

### Parallel Execution

```
      → Step A →
Input             → Output
      → Step B →
```

Used when:

- Tasks are independent

---

### Conditional Execution

```
Input → Classifier → Branch → Output
```

Used when:

- Logic depends on model output

---

## Modern LangChain Design

This project uses **modern LangChain architecture:**

- Runnable API
- PromptTemplate
- Output Parsers
- RunnableParallel
- RunnableBranch
- Structured Outputs

No deprecated components like:

- LLMChain
- SequentialChain
- AgentExecutor-based chains

---

## Real World Applications

### Sequential Chains

- Document summarization
- Data pipelines
- Research assistants
- RAG pipelines

---

### Parallel Chains

- Multi-analysis systems
- Evaluation pipelines
- Multi-agent subtasks

---

### Conditional Chains

- AI assistants
- Agent routing
- Decision trees
- Tool selection

---

## Folder Structure

```
chains/
│
├── sequential_chain.py
├── parallel_chain.py
├── conditional_chain.py
│
└── README.md
```

---

## Example Model

All chains use:

```
meta-llama/Llama-4-Scout-17B-16E-Instruct
```

Accessed through:

```
HuggingFaceEndpoint
```

---

## Future Improvements

Possible extensions:

- Streaming chains
- Async chains
- LangGraph migration
- Tool-integrated chains
- Memory integration
- RAG chains
- Evaluation pipelines

---

## Author

LangChain experimentation project focused on learning:

- Modern LangChain
- Agents
- Tools
- Chains
- Structured Outputs
- LLM Architecture

---

## Notes

This repository focuses on **practical LangChain engineering patterns** rather than toy examples.

The goal is to cover the **core building blocks required to build production-grade AI systems.**