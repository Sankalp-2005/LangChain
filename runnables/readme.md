# LangChain Runnables

This module demonstrates the **Runnable system in modern LangChain**.

Runnables are the **core abstraction in modern LangChain architecture** and replace older components such as:

- LLMChain
- SequentialChain
- SimpleSequentialChain
- RouterChain

Runnables allow you to build structured LLM workflows using composable components.

This folder covers the most important Runnable types:

- RunnableSequence
- RunnableParallel
- RunnableBranch
- RunnableLambda
- RunnablePassthrough

These components form the foundation for building:

- Chains
- Agents
- Tools
- RAG pipelines
- AI workflows

---

## Overview

A Runnable represents a **unit of computation** that transforms input into output.

Basic Runnable pipeline:

```
Input → Runnable → Output
```

Example:

```
Input → Prompt → Model → Parser → Output
```

Runnable pipelines can be composed:

```
chain = step1 | step2 | step3
```

or using:

```
RunnableSequence(...)
```

---

## Folder Structure

```
runnables/
│
├── sequence_runnable.py
├── parallel_runnable.py
├── branch_runnable.py
├── lambda_runnable.py
├── passthrough_runnable.py
├── demo_code.py
│
└── README.md
```

---

# Runnable Types Covered

| Runnable | Purpose |
|---------|---------|
| RunnableSequence | Sequential execution |
| RunnableParallel | Parallel execution |
| RunnableBranch | Conditional execution |
| RunnableLambda | Custom Python logic |
| RunnablePassthrough | Forward input unchanged |

---

# 1. RunnableSequence

File:

```
sequence_runnable.py
```

RunnableSequence executes components **one after another**.

Output of one step becomes input to the next. :contentReference[oaicite:0]{index=0}

---

## Architecture

```
Task
  ↓
Prompt Template
  ↓
LLM
  ↓
Parser
  ↓
Explanation Prompt
  ↓
LLM
  ↓
Output
```

---

## Implementation

Example:

```python
chain = RunnableSequence(
    template_code,
    model,
    string_parser,
    template_explain,
    model,
    string_parser
)
```

The sequence:

1. Generates code
2. Explains code
3. Returns explanation

---

## Use Cases

- Multi-step reasoning
- Data processing pipelines
- Summarization workflows
- Code generation pipelines

---

# 2. RunnableParallel

File:

```
parallel_runnable.py
```

RunnableParallel executes multiple tasks **simultaneously**. :contentReference[oaicite:1]{index=1}

Each branch receives the same input.

---

## Architecture

```
Task
  ↓
 ┌───────────────┐
 │               │
Manual Code   Inbuilt Code
 │               │
 └──────┬────────┘
        ↓
      Output
```

---

## Implementation

```python
parallel_chain = RunnableParallel(
{
    "manual": RunnableSequence(template_manual|model|parser),
    "inbuilt": RunnableSequence(template_inbuilt|model|parser)
}
)
```

---

## Use Cases

- Multiple solutions
- Multi-perspective reasoning
- Evaluation pipelines
- Comparison systems

---

# 3. RunnableBranch

File:

```
branch_runnable.py
```

RunnableBranch allows **conditional execution** based on input. :contentReference[oaicite:2]{index=2}

---

## Architecture

```
Topic
   ↓
Text Generator
   ↓
Branch Condition
   ↓
 ┌─────────────┐
 │             │
Summary      Original Text
 │             │
 └──────┬──────┘
        ↓
      Output
```

---

## Implementation

```python
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500,
     RunnableSequence(template_summarizer,model,string_parser)),
    RunnablePassthrough()
)
```

If text length > 500 words:

```
Generate summary
```

Otherwise:

```
Return original text
```

---

## Use Cases

- Routing logic
- Conditional processing
- Agent decision logic
- Content filtering

---

# 4. RunnableLambda

File:

```
lambda_runnable.py
```

RunnableLambda allows you to integrate **custom Python functions** into Runnable pipelines. :contentReference[oaicite:3]{index=3}

---

## Architecture

```
Task
   ↓
LLM Code Generator
   ↓
Generated Code
   ↓
 ┌─────────────┐
 │             │
Return Code   Save File
```

---

## Implementation

```python
parallel_chain = RunnableParallel({
    "code": RunnablePassthrough(),
    "file": RunnableLambda(code_creator)
})
```

The lambda function:

```python
def code_creator(text):
    with open("demo_code.py","w") as code_file:
        code_file.write(text)
```

The Runnable:

- Returns generated code
- Saves code to file

---

## Use Cases

- File operations
- API calls
- Data transformations
- Custom logic
- Tool building

---

# 5. RunnablePassthrough

File:

```
passthrough_runnable.py
```

RunnablePassthrough forwards input **without modification**. :contentReference[oaicite:4]{index=4}

Useful when input must be reused in multiple steps.

---

## Architecture

```
Task
  ↓
Code Generator
  ↓
Generated Code
  ↓
 ┌──────────────┐
 │              │
Return Code   Explain Code
```

---

## Implementation

```python
parallel_chain = RunnableParallel({
    "code": RunnablePassthrough(),
    "explain": RunnableSequence(...)
})
```

The passthrough branch returns:

```
Generated code
```

The second branch returns:

```
Explanation
```

---

# Runnable Graph Visualization

Runnable pipelines can be visualized:

```python
chain.get_graph().print_ascii()
```

Example Output:

```
Prompt → Model → Parser → Branch → Output
```

This helps debug pipeline architecture.

---

# Installation

Install dependencies:

```bash
pip install langchain
pip install langchain-core
pip install langchain-huggingface
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

## Sequence Runnable

```
python sequence_runnable.py
```

Example Output:

```
Code explanation of GCD algorithm...
```

---

## Parallel Runnable

```
python parallel_runnable.py
```

Example Output:

```
Manual Code:
...

Inbuilt Code:
...
```

---

## Branch Runnable

```
python branch_runnable.py
```

Example Output:

```
Generated report or summary depending on length
```

---

## Lambda Runnable

```
python lambda_runnable.py
```

Example Output:

```
Generated Python code
```

Also creates:

```
demo_code.py
```

---

## Passthrough Runnable

```
python passthrough_runnable.py
```

Example Output:

```
Generated Code:
...

Explanation:
...
```

---

# Modern LangChain Design

This project uses **modern LangChain architecture (Runnable-based)**:

- RunnableSequence
- RunnableParallel
- RunnableBranch
- RunnableLambda
- RunnablePassthrough

These are the building blocks of:

- Chains
- Agents
- Tools
- RAG systems
- LangGraph workflows

---

# Key Concepts Learned

## Runnable

A Runnable transforms input into output:

```
Input → Runnable → Output
```

---

## Composition

Runnables can be chained:

```
prompt | model | parser
```

---

## Sequential Execution

```
Step A → Step B → Step C
```

---

## Parallel Execution

```
Input → Multiple Tasks → Output
```

---

## Conditional Execution

```
Input → Decision → Branch
```

---

## Custom Logic

```
RunnableLambda → Python Function
```

---

# Real World Applications

### RunnableSequence

- RAG pipelines
- Research assistants
- Data pipelines

---

### RunnableParallel

- Multi-agent workflows
- Evaluation systems
- Comparison tools

---

### RunnableBranch

- Agent routing
- Tool selection
- Decision systems

---

### RunnableLambda

- Tool creation
- API integration
- Automation systems

---

### RunnablePassthrough

- Multi-output pipelines
- Context reuse
- Data routing

---

# Future Improvements

Possible extensions:

- Streaming runnables
- Async runnables
- Tool integration
- Agent workflows
- LangGraph migration
- Stateful pipelines

---

# Author

LangChain experimentation project focused on learning:

- Runnable Architecture
- LangChain Core
- Chains
- Agents
- Retrieval Systems

---

# Notes

Runnables are the **foundation of modern LangChain**.

Understanding Runnables makes it easier to build:

- Chains
- Agents
- Tools
- RAG pipelines
- Production AI systems