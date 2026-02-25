# LangChain Tool Calling

This module demonstrates **Tool Calling in LangChain**, one of the most important capabilities for building **AI Agents and intelligent assistants**.

Tool calling allows Large Language Models (LLMs) to **invoke external functions** to perform tasks that cannot be solved using text generation alone.

Instead of guessing answers, the LLM can:

- Call APIs
- Perform calculations
- Access databases
- Execute logic
- Fetch real-time data

This folder demonstrates practical implementations of **LangChain Tool Calling using modern `.bind_tools()` architecture.**

---

## Overview

Large Language Models are powerful but limited:

- No real-time data
- No computation reliability
- No external actions

Tool calling solves this problem:

```
User Query
   ↓
LLM
   ↓
Tool Selection
   ↓
Tool Execution
   ↓
LLM Final Answer
```

Example:

```
User:
Convert 100 USD to INR
```

Pipeline:

```
LLM → Exchange Rate API → Calculation → Answer
```

---

## Folder Structure

```
tool_calling/
│
├── tool_bindings.py
├── currency_converter.py
│
└── README.md
```

---

## Tool Calling Workflow

Tool calling follows a structured process:

```
1. User Input
2. Model decides tool
3. Tool execution
4. Tool result returned
5. Model generates final response
```

Pipeline:

```
User
 ↓
LLM
 ↓
Tool Call
 ↓
Tool Result
 ↓
LLM Response
```

---

# Tool Calling Components

| Component | Purpose |
|----------|---------|
| Tool Function | External functionality |
| Tool Binding | Connect tools to model |
| Tool Calls | Model tool requests |
| Tool Execution | Running tools |
| Final Response | LLM-generated answer |

---

# 1. Basic Tool Calling

File:

```
tool_bindings.py
```

This example demonstrates **basic tool calling with a mathematical function.**

A simple multiplication tool is defined and bound to the model. :contentReference[oaicite:0]{index=0}

---

## Tool Definition

```python
@tool
def multiply(a:int,b:int)->int:
    """Function to multiply two numbers"""
```

The `@tool` decorator converts a Python function into a LangChain tool.

---

## Tool Binding

```python
model_with_tool = model.bind_tools([multiply])
```

This allows the model to use the tool. :contentReference[oaicite:1]{index=1}

---

## Tool Calling Flow

```
User Query
   ↓
Model selects multiply tool
   ↓
Tool executes multiplication
   ↓
Result returned
   ↓
Model produces answer
```

---

## Tool Execution

```python
result_tool = multiply.invoke(result_ai.tool_calls[0])
```

The tool is executed manually. :contentReference[oaicite:2]{index=2}

---

## Example Input

```
What is 3 multiplied by 10
```

Example Output:

```
30
```

---

# 2. Multi-Tool Calling (Currency Converter)

File:

```
currency_converter.py
```

This example demonstrates **multiple tool calls with dependency between tools.**

Two tools are used:

- Exchange rate fetcher
- Currency converter

---

## Tool 1 — Exchange Rate Tool

```python
@tool
def get_conversion_factor(base_currency:str,
                          target_currency:str)->float:
```

This tool fetches real-time exchange rates using an API. :contentReference[oaicite:3]{index=3}

---

## API Used

```
ExchangeRate API
```

Endpoint:

```
https://v6.exchangerate-api.com
```

---

## Tool 2 — Conversion Tool

```python
@tool
def convert(amount:int,
            rate:Annotated[float,InjectedToolArg])->float:
```

This tool multiplies the amount by the conversion rate. :contentReference[oaicite:4]{index=4}

---

## Injected Tool Arguments

This example uses:

```
InjectedToolArg
```

Example:

```python
rate: Annotated[float, InjectedToolArg]
```

This allows one tool to pass results to another tool.

---

## Tool Binding

```python
model_with_tools = model.bind_tools(
[
    get_conversion_factor,
    convert
])
```

---

## Tool Calling Flow

```
User:
Convert 100 USD to INR
```

Pipeline:

```
LLM
 ↓
get_conversion_factor
 ↓
Exchange API
 ↓
Conversion Rate
 ↓
convert tool
 ↓
Final Value
 ↓
LLM Answer
```

---

## Manual Tool Execution

```python
for tool_call in ai_message.tool_calls:

    if tool_call["name"]=="get_conversion_factor":

        tool_message_1 = get_conversion_factor.invoke(tool_call)

        conversion_rate = json.loads(
            tool_message_1.content
        )["conversion_rate"]

    elif tool_call["name"]=="convert":

        tool_call["args"]["conversion_rate"] = conversion_rate

        tool_message_2 = convert.invoke(tool_call)
```

This executes tools in sequence. :contentReference[oaicite:5]{index=5}

---

## Example Input

```
Convert 100 USD to INR
```

Example Output:

```
100 USD is approximately 8300 INR
```

(Depends on live exchange rate)

---

# Key Concepts

## Tools

Tools are Python functions that the LLM can call:

```
LLM → Tool → Result
```

---

## Tool Decorator

```python
@tool
```

Converts functions into LangChain tools.

---

## Tool Binding

```
model.bind_tools()
```

Connects tools to the model.

---

## Tool Calls

The model produces:

```python
ai_message.tool_calls
```

Example:

```
multiply(a=3,b=10)
```

---

## Tool Execution

Tools are executed manually:

```
tool.invoke()
```

---

## Injected Arguments

```
InjectedToolArg
```

Allows:

```
Tool → Tool data passing
```

Important for:

- Multi-step workflows
- Agents
- Pipelines

---

# Installation

Install dependencies:

```bash
pip install langchain
pip install langchain-core
pip install langchain-google-genai
pip install python-dotenv
pip install requests
```

---

# Environment Setup

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
Exchange_rate_api_key=your_api_key_here
```

---

# Usage

## Basic Tool Calling

```
python tool_bindings.py
```

Example Output:

```
30
```

---

## Currency Converter Tool

```
python currency_converter.py
```

Example Output:

```
100 USD ≈ 8300 INR
```

---

# Modern LangChain Design

This project uses **modern LangChain tool calling architecture:**

- `.bind_tools()`
- Tool decorators
- Tool calls
- Tool messages
- InjectedToolArg

No deprecated agent-based tool calling used.

---

# Key Concepts Learned

## Tool Calling

```
LLM → Tool → LLM
```

---

## Tool Selection

LLM decides:

```
Which tool to use
```

---

## Tool Execution

External logic:

```
API calls
Calculations
Logic
```

---

## Multi Tool Pipelines

```
Tool A → Tool B → Result
```

---

# Real World Applications

Tool calling is used in:

- AI Agents
- ChatGPT plugins
- AI assistants
- Automation bots
- Financial assistants
- Research assistants

---

# Future Improvements

Possible extensions:

- Automatic tool execution
- Agent-based tool calling
- LangGraph tools
- Tool routing
- Tool memory
- Multi-agent tools

---

# Author

LangChain experimentation project focused on learning:

- Tool Calling
- Agents
- APIs
- Automation
- Modern LangChain Architecture

---

# Notes

Tool calling is one of the core building blocks of **AI Agents**.

Agents are essentially:

```
LLM + Tools + Memory + Planning
```

Understanding tool calling is essential before building advanced agent systems.