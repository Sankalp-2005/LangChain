# LangChain Chatbots

This module demonstrates how to build **stateful conversational chatbots using modern LangChain architecture.**

It covers:

- Basic conversational chatbot with message history
- Persistent chat history
- Session-based chatbots
- Dynamic prompts using ChatPromptTemplate

These examples use **LangChain Chat Models + Message Objects**, which represent the modern approach to building conversational AI systems.

---

## Overview

A chatbot is an AI system that maintains **conversation context across multiple messages.**

Unlike single LLM calls, chatbots require:

- Message history
- Role-based messages
- Session management
- Dynamic prompts
- Persistent memory

This module demonstrates the **core building blocks required to build production-grade chatbots.**

---

## Architecture

Modern LangChain chatbots use **Message-Based Architecture.**

Each conversation consists of structured messages:

```
System Message → Defines behavior
Human Message → User input
AI Message → Model response
```

Example:

```
System: You are a helpful assistant
User: Hello
AI: Hello! How can I help?
User: What is AI?
AI: Artificial Intelligence is...
```

LangChain represents this as:

```python
[
    SystemMessage(),
    HumanMessage(),
    AIMessage()
]
```

---

## Files

```
chatbots/
│
├── chatbot_history.py
├── chatbot_session.py
├── history.txt
│
└── README.md
```

---

## 1. chatbot_history.py

Implements a **basic conversational chatbot with in-memory history.**

This example demonstrates the simplest way to build a chatbot using LangChain message objects.

:contentReference[oaicite:0]{index=0}

---

### Architecture

```
User Input
   ↓
Append to History
   ↓
LLM
   ↓
Response
   ↓
Append Response
   ↓
Next Interaction
```

---

### Key Components

#### Message History

```python
history = [
    SystemMessage(content="You are a helpful assistant")
]
```

The conversation history is stored as a list of messages.

Each interaction appends:

```python
history.append(HumanMessage(content=user_input))
history.append(AIMessage(content=response))
```

---

### Features

- Stateful conversation
- Message-based architecture
- Interactive terminal chatbot
- Manual history tracking

---

### Execution

```bash
python chatbot_history.py
```

---

### Example

```
You: hello
AI: Hello! How can I help you today?

You: What is a DoS attack?
AI: A DoS attack is a cyberattack that attempts to make a service unavailable.
```

---

### When To Use

This design is ideal for:

- Learning LangChain chat models
- Simple chatbots
- Prototypes
- Experiments

---

## 2. chatbot_session.py

Implements a **session-based chatbot with persistent history.**

This example demonstrates how to maintain chat history across sessions.

:contentReference[oaicite:1]{index=1}

---

### Architecture

```
history.txt
    ↓
Load Chat History
    ↓
ChatPromptTemplate
    ↓
LLM
    ↓
Response
    ↓
Append Messages
```

---

### ChatPromptTemplate

Dynamic prompts are created using:

```python
ChatPromptTemplate([
    ("system","You are a helpful assistant"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{query}")
])
```

This allows:

- Automatic history injection
- Dynamic conversation context
- Clean prompt design

---

### Message Placeholder

```
MessagesPlaceholder(variable_name="chat_history")
```

This component inserts the full conversation history into the prompt.

---

### Persistent History

Chat history is loaded from a file:

:contentReference[oaicite:2]{index=2}

```python
with open("history.txt","r") as f:
    chat_history.extend(f.readlines())
```

This allows:

- Session restoration
- Persistent memory
- Conversation continuity

---

### Execution

```bash
python chatbot_session.py
```

---

### Features

- Persistent chat history
- Dynamic prompts
- Session restoration
- Structured conversation

---

## Message Types

LangChain chatbots use structured messages:

| Message Type | Purpose |
|------------|---------|
| SystemMessage | Defines assistant behavior |
| HumanMessage | User input |
| AIMessage | Model response |

Example:

```python
SystemMessage(content="You are helpful")
HumanMessage(content="Hello")
AIMessage(content="Hi!")
```

---

## Technologies Used

| Technology | Purpose |
|----------|---------|
| LangChain Core | Chat Architecture |
| HuggingFace Endpoint | LLM Access |
| Chat Models | Conversation Handling |
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

### Basic Chatbot

```
python chatbot_history.py
```

Commands:

```
exit → terminates chatbot
```

---

### Session Chatbot

```
python chatbot_session.py
```

Loads history from:

```
history.txt
```

---

## Example Conversation

```
You: hello
AI: Hello. How can I help you today?

You: What is a DoS attack?
AI: A DoS attack is a cyberattack where a system is overwhelmed with requests.

You: Who does it?
AI: Hackers, cybercriminals, nation-state actors, and botnets commonly perform DoS attacks.
```

---

## Modern LangChain Design

This project uses **modern LangChain architecture:**

- Chat Models
- Message Objects
- ChatPromptTemplate
- MessagesPlaceholder
- Stateful Conversations

No deprecated components like:

- ConversationChain
- Memory classes
- AgentExecutor-based chatbots

---

## Design Patterns

### Pattern 1 — Manual History Management

```
history = []
history.append(HumanMessage)
history.append(AIMessage)
```

Advantages:

- Full control
- Simple design
- Easy debugging

---

### Pattern 2 — Prompt-Based History Injection

```
ChatPromptTemplate + MessagesPlaceholder
```

Advantages:

- Clean architecture
- Scalable
- Production-ready

---

## Real World Applications

### Customer Support Bots

- Persistent conversations
- Session tracking

---

### AI Assistants

- Context-aware responses
- Multi-turn reasoning

---

### Personal AI Systems

- Long-term interaction
- User personalization

---

### Educational Bots

- Continuous learning sessions
- Context tracking

---

## Key Concepts Learned

### Chat Models

Chat models operate on message lists:

```python
model.invoke(messages)
```

Instead of:

```
model.invoke(text)
```

---

### Stateful Conversations

Chatbots maintain:

```
Previous Messages → Current Response
```

---

### Prompt Engineering

System messages define behavior:

```python
SystemMessage(
    content="You are a helpful assistant"
)
```

---

### Persistent Memory

Chat history stored in:

```
history.txt
```

Allows:

- Conversation recovery
- Long-term sessions

---

## Model Used

Both chatbots use:

```
meta-llama/Llama-3.3-70B-Instruct
```

Accessed through:

```
HuggingFaceEndpoint
```

---

## Future Improvements

Possible extensions:

- Database memory
- Vector memory
- Long-term memory
- RAG chatbot
- Streaming responses
- GUI chatbot
- Voice chatbot
- Multi-user sessions
- LangGraph chatbot

---

## Author

LangChain experimentation project focused on learning:

- Modern LangChain
- Agents
- Tools
- Chains
- Chatbots
- LLM Architecture

---

## Notes

This repository focuses on **practical chatbot engineering patterns** rather than simple examples.

The goal is to understand how **real conversational AI systems are built.**