# LangChain Structured Output

This module demonstrates **Structured Output techniques in LangChain**.

Structured output allows Large Language Models (LLMs) to return **well-defined data formats instead of plain text**.

Instead of generating unstructured responses:

```
"The college was established in 2000 and is located near Hyderabad..."
```

Structured output produces:

```json
{
  "college_name": "CVR College of Engineering",
  "college_established_year": 2000,
  "college_location": "Hyderabad, India"
}
```

Structured output is essential for building:

- AI Agents
- Automation Systems
- APIs
- Data Pipelines
- Production AI Applications

---

## Overview

LLMs normally produce **free-form text**, which is difficult to parse reliably.

Structured output solves this problem:

```
User Input
   ↓
LLM
   ↓
Schema Validation
   ↓
Structured Data
```

This module demonstrates three major approaches:

- JSON Schema Structured Output
- Pydantic Structured Output
- TypedDict Structured Output

---

## Folder Structure

```
structured_output/
│
├── json_structured_output.py
├── pydantic_structured_output.py
├── typedict.py
├── pydantic_test.py
├── college_details.json
│
└── README.md
```

---

## Structured Output Methods

| Method | Type Safety | Validation | Ease of Use |
|-------|-------------|------------|-------------|
| JSON Schema | Medium | Medium | Medium |
| TypedDict | Medium | Low | Easy |
| Pydantic | High | High | Best |

---

# 1. JSON Schema Structured Output

File:

```
json_structured_output.py
```

This approach uses a **JSON Schema** to define the structure of the LLM output. :contentReference[oaicite:0]{index=0}

---

## JSON Schema Example

Schema definition:

```json
{
 "title": "college_details",
 "type": "object",
 "properties": {
   "college_name": "string",
   "college_established_year": "integer",
   "college_location": "string"
 }
}
```

Example schema file: :contentReference[oaicite:1]{index=1}

```
college_details.json
```

---

## Implementation

```python
structuerd_model = model.with_structured_output(json)
```

The model automatically produces structured output. :contentReference[oaicite:2]{index=2}

---

## Example Input

```
CVR College of Engineering was established in 2000...
```

Example Output:

```json
{
 "college_name": "CVR College of Engineering",
 "college_established_year": 2000,
 "college_location": "Hyderabad, India"
}
```

---

## Advantages

- Language independent
- Flexible
- API-friendly

---

## Limitations

- No strong type validation
- Less Pythonic
- Harder to maintain

---

# 2. Pydantic Structured Output

File:

```
pydantic_structured_output.py
```

Pydantic provides **strongly typed structured output** with validation. :contentReference[oaicite:3]{index=3}

This is the **recommended approach** for most LangChain applications.

---

## Pydantic Model

```python
class college_details(BaseModel):

    college_name: str
    college_established_year: int
    college_location: str
    courses_offered: list[str]
    minor_courses: Optional[list[str]]
    country: Optional[Literal["India","Out side India"]]
```

The model defines:

- Data types
- Optional fields
- Allowed values
- Field descriptions

---

## Implementation

```python
structured_model = model.with_structured_output(college_details)
```

The model returns a validated object. :contentReference[oaicite:4]{index=4}

---

## Example Output

```python
college_details(
  college_name='CVR College of Engineering',
  college_established_year=2000,
  college_location='Hyderabad, India',
  courses_offered=[...],
  minor_courses=[...],
  country='India'
)
```

---

## Advantages

- Strong type checking
- Automatic validation
- Python objects
- Best reliability

---

## Why Pydantic is Best

Pydantic ensures:

```
Correct Types
Valid Values
Required Fields
```

Example:

```
college_established_year must be integer
```

Invalid outputs are rejected automatically.

---

# 3. TypedDict Structured Output

File:

```
typedict.py
```

TypedDict provides lightweight structured output definitions. :contentReference[oaicite:5]{index=5}

---

## TypedDict Model

```python
class college_details(TypedDict):

    college_name: str
    college_established_year: int
    college_location: str
    courses_offered: list[str]
    minor_courses: Optional[list[str]]
    country: Optional[Literal["India","Out side India"]]
```

Descriptions are provided using `Annotated`.

---

## Implementation

```python
structured_model = model.with_structured_output(college_details)
```

The model returns structured dictionaries. :contentReference[oaicite:6]{index=6}

---

## Example Output

```python
{
 "college_name": "CVR College of Engineering",
 "college_established_year": 2000,
 "college_location": "Hyderabad, India",
 "courses_offered": [...],
 "minor_courses": [...],
 "country": "India"
}
```

---

## Advantages

- Simple
- Lightweight
- Easy to write

---

## Limitations

- Weak validation
- No runtime type enforcement

---

# 4. Pydantic Validation Example

File:

```
pydantic_test.py
```

This file demonstrates **Pydantic data validation and conversion**. :contentReference[oaicite:7]{index=7}

---

## Example Model

```python
class person_details(BaseModel):

    name: str
    age: int = Field(gt=20, lt=60)
    address: Optional[str]
    email: EmailStr
```

Validation includes:

- Type checking
- Range checking
- Email validation

---

## Example Validation

```python
person = person_details(**new_person)
```

Pydantic automatically:

- Converts types
- Validates values
- Enforces constraints

Example features: :contentReference[oaicite:8]{index=8}

- Email validation
- Default values
- Range constraints
- Optional fields

---

## Example Output Formats

Dictionary:

```python
dict(person)
```

JSON:

```python
person.model_dump_json()
```

---

# Installation

Install dependencies:

```bash
pip install langchain
pip install langchain-core
pip install langchain-google-genai
pip install python-dotenv
pip install pydantic
```

---

# Environment Setup

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

# Usage

## JSON Structured Output

```
python json_structured_output.py
```

---

## Pydantic Structured Output

```
python pydantic_structured_output.py
```

---

## TypedDict Structured Output

```
python typedict.py
```

---

## Pydantic Validation Example

```
python pydantic_test.py
```

---

# Modern LangChain Design

This project uses **modern LangChain structured output patterns**:

- `.with_structured_output()`
- Schema-based outputs
- Pydantic models
- TypedDict schemas

No deprecated parsers used.

---

# Key Concepts Learned

## Structured Output

Instead of:

```
Text Output
```

We get:

```
Validated Data Objects
```

---

## Schema Enforcement

Schema defines:

```
Fields
Types
Rules
```

---

## Validation

Ensures:

```
Correct Types
Valid Values
Required Fields
```

---

## Reliability

Structured output reduces:

- Parsing errors
- Hallucinations
- Invalid responses

---

# Real World Applications

### Structured Output is Used In

- AI Agents
- Tool Calling
- APIs
- Data Extraction
- Automation Systems
- Knowledge Graph Building

---

# Comparison

| Method | Best Use Case |
|-------|--------------|
| JSON Schema | APIs |
| TypedDict | Simple Projects |
| Pydantic | Production Systems |

---

# Future Improvements

Possible extensions:

- Tool calling schemas
- Function calling
- OpenAI structured outputs
- Agent schemas
- Guardrails integration
- Schema versioning

---

# Author

LangChain experimentation project focused on learning:

- Structured Outputs
- LLM Reliability
- Data Validation
- Modern LangChain Architecture

---

# Notes

Structured output is one of the most important techniques for building **reliable LLM applications**.

Most production AI systems rely on **schema-based outputs instead of raw text generation.**