# LangChain Tools

This module demonstrates **Tools in LangChain**, one of the fundamental building blocks for **AI Agents and Tool Calling systems**.

Tools allow Large Language Models (LLMs) to interact with **external functionality**, including:

- APIs
- Calculations
- Databases
- Search engines
- Shell commands
- Custom logic

This folder demonstrates different ways to create and use tools in modern LangChain:

- Tool Decorator (`@tool`)
- StructuredTool
- BaseTool Class
- Toolkits
- Built-in Tools

These represent the **core patterns used in real-world LangChain applications.**

---

## Overview

Tools are Python functions or classes that expose functionality to LLMs.

Basic tool workflow:

```
User Query
   ↓
LLM
   ↓
Tool Selection
   ↓
Tool Execution
   ↓
Result
```

Example:

```
User:
Multiply 3 and 5
```

Pipeline:

```
LLM → Multiply Tool → Result
```

---

## Folder Structure

```
tools/
│
├── tools_user_defined.py
├── structured_tools.py
├── base_tools_class_tools.py
├── tool_kit.py
├── tools_inbuilt.py
│
└── README.md
```

---

## Tool Types Covered

| Tool Type | Method | Complexity |
|---------|--------|------------|
| Decorator Tools | `@tool` | Easy |
| Structured Tools | StructuredTool | Medium |
| BaseTool Tools | BaseTool class | Advanced |
| Toolkits | Tool Collections | Medium |
| Built-in Tools | LangChain tools | Easy |

---

# 1. User Defined Tools (@tool)

File:

```
tools_user_defined.py
```

This example demonstrates how to create tools using the `@tool` decorator. :contentReference[oaicite:0]{index=0}

---

## Tool Definition

```python
@tool
def multiply(a:int,b:int)->int:
```

The decorator converts a Python function into a LangChain tool.

---

## Tool Execution

```python
result = multiply.invoke({"a":3,"b":5})
```

The tool executes independently. :contentReference[oaicite:1]{index=1}

---

## Tool Metadata

Tools automatically generate metadata:

```python
multiply.name
multiply.description
multiply.args
multiply.args_schema.model_json_schema()
```

This metadata allows LLMs to understand how to use the tool.

---

## Example Output

```
15
Multiply
Function to multiply two numbers
```

---

## Advantages

- Simple
- Quick setup
- Ideal for small tools

---

## Use Cases

- Math tools
- Utility functions
- Quick prototypes

---

# 2. Structured Tools

File:

```
structured_tools.py
```

StructuredTools provide **schema-based tool definitions** using Pydantic. :contentReference[oaicite:2]{index=2}

---

## Input Schema

```python
class MultiplyInput(BaseModel):

    a:int
    b:int
```

Defines:

- Tool parameters
- Data types
- Validation rules

---

## Tool Creation

```python
multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="Multiply",
    description="Multiply Two numbers",
    args_schema=MultiplyInput
)
```

---

## Tool Execution

```python
multiply_tool.invoke({"a":3,"b":5})
```

StructuredTools enforce input validation. :contentReference[oaicite:3]{index=3}

---

## Advantages

- Strong validation
- Clear schemas
- Production-ready

---

## Use Cases

- APIs
- Agents
- Data pipelines

---

# 3. BaseTool Class Tools

File:

```
base_tools_class_tools.py
```

This example demonstrates building tools by extending the **BaseTool class**. :contentReference[oaicite:4]{index=4}

---

## Tool Schema

```python
class MultiplyInput(BaseModel):

    a:int
    b:int
```

---

## Tool Class

```python
class Multiply(BaseTool):

    name = "Multiply"
    description = "Multiply two numbers"
    args_schema = MultiplyInput

    def _run(self,a:int,b:int)->int:
        return a*b
```

---

## Tool Execution

```python
multiply_tool = Multiply()

result = multiply_tool.invoke({"a":3,"b":5})
```

BaseTool provides full control. :contentReference[oaicite:5]{index=5}

---

## Advantages

- Maximum flexibility
- Full customization
- Advanced control

---

## Use Cases

- Complex tools
- Custom integrations
- Production agents

---

# 4. Toolkits

File:

```
tool_kit.py
```

Toolkits group multiple tools into collections. :contentReference[oaicite:6]{index=6}

---

## Tool Definitions

```python
@tool
def multiply(a:int,b:int)->int:
```

```python
@tool
def add(a:int,b:int)->int:
```

---

## Toolkit Class

```python
class MathToolKit:

    def get_tools(self):
        return [add,multiply]
```

---

## Toolkit Usage

```python
toolkit = MathToolKit()

tools = toolkit.get_tools()
```

Toolkits simplify tool management. :contentReference[oaicite:7]{index=7}

---

## Advantages

- Organized tools
- Scalable
- Agent-friendly

---

## Use Cases

- Agent tool collections
- Modular systems
- Large projects

---

# 5. Built-in Tools

File:

```
tools_inbuilt.py
```

This example demonstrates **built-in LangChain tools.** :contentReference[oaicite:8]{index=8}

---

## DuckDuckGo Search Tool

```python
from langchain_community.tools import DuckDuckGoSearchRun
```

Example:

```python
search_tool.invoke("What is the weather in Hyderabad")
```

Performs web search. :contentReference[oaicite:9]{index=9}

---

## Shell Tool

```python
from langchain_community.tools import ShellTool
```

Example:

```python
shell_tool.invoke("pip install flask")
```

Executes terminal commands. :contentReference[oaicite:10]{index=10}

---

## Advantages

- Ready-to-use
- Reliable
- Fast setup

---

## Use Cases

- Web search agents
- Automation agents
- DevOps assistants

---

# Tool Comparison

| Method | Flexibility | Difficulty | Best Use |
|-------|-------------|-----------|----------|
| @tool | Medium | Easy | Simple tools |
| StructuredTool | High | Medium | Agents |
| BaseTool | Very High | Hard | Advanced tools |
| Toolkit | High | Medium | Multi-tool systems |
| Built-in Tools | Medium | Easy | Fast development |

---

# Installation

Install dependencies:

```bash
pip install langchain
pip install langchain-core
pip install langchain-community
pip install python-dotenv
pip install pydantic
pip install duckduckgo-search
```

---

# Usage

## User Defined Tool

```
python tools_user_defined.py
```

---

## Structured Tool

```
python structured_tools.py
```

---

## BaseTool Tool

```
python base_tools_class_tools.py
```

---

## Toolkit

```
python tool_kit.py
```

---

## Built-in Tools

```
python tools_inbuilt.py
```

---

# Modern LangChain Design

This project uses **modern LangChain tool architecture:**

- Tool decorator
- StructuredTool
- BaseTool
- Toolkits
- Built-in tools

These are used in:

- Tool Calling
- Agents
- LangGraph
- Automation Systems

---

# Key Concepts Learned

## Tool

A tool is:

```
Python Function → Callable by LLM
```

---

## Tool Schema

Defines:

```
Parameters
Types
Descriptions
```

---

## Tool Metadata

Tools expose:

```
Name
Description
Arguments
Schema
```

LLMs use this metadata to decide tool usage.

---

## Tool Invocation

```
tool.invoke()
```

Executes tool logic.

---

## Tool Collections

```
Toolkit → Multiple Tools
```

Used in agents.

---

# Real World Applications

Tools are used in:

- AI Agents
- Automation systems
- Financial assistants
- Coding assistants
- Search assistants
- DevOps bots

---

# Future Improvements

Possible extensions:

- Tool calling agents
- LangGraph tools
- Async tools
- Tool caching
- Tool routing
- Multi-agent tools

---

# Author

LangChain experimentation project focused on learning:

- Tools
- Tool Calling
- Agents
- Automation
- Modern LangChain Architecture

---

# Notes

Tools are the foundation of **AI Agents**.

Agents are built using:

```
LLM + Tools + Memory + Planning
```

Understanding tools is essential before building advanced **agent-based systems.**