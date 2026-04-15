# resume-screener

## 📄 AI Resume Screening System

An automated, AI-powered pipeline designed to evaluate candidate resumes against a specific job description. This system extracts key skills, matches them with role requirements, and generates a quantitative fit score alongside a detailed explanation. 

Built using LangChain's Expression Language (LCEL) and fully traced with LangSmith for debugging and observability.

## 🚀 Features

* **Skill Extraction:** Uses structured JSON generation to parse skills, tools, and experience objectively.
* **Intelligent Matching Logic:** Compares candidate profiles directly against job requirements without hallucinating missing skills.
* **Scoring & Explanation:** Assigns a strict 0-100 fit score and provides a step-by-step reasoning for the evaluation.
* **Pipeline Observability:** Fully integrated with LangSmith to trace prompts, intermediate outputs, and execution times.

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** LangChain (LCEL)
* **Validation:** Pydantic
* **LLM Gateway:** OpenRouter (using `openai/gpt-4o-mini`)
* **Tracing:** LangSmith

## 📁 Project Structure

```text
resume-screener/
├── data/
│   ├── resumes/            # Text files of strong, average, and weak candidates
│   └── job_description.txt # Target role requirements
├── prompts/
│   ├── __init__.py         # Package initializer
│   └── templates.py        # Anti-hallucination prompt engineering
├── chains/
│   ├── __init__.py         # Package initializer
│   ├── models.py           # Pydantic schemas for strict JSON output
│   └── pipeline.py         # LCEL extraction and evaluation chain
├── main.py                 # Execution script and LangSmith tracing
├── setup_data.py           # Script to generate dummy data
└── requirements.txt        # Project dependencies
```



## ⚙️ Setup & Installation

### 1. Clone the repository

```
git clone https://github.com/VishwaG1t/resume-screener.git
cd resume-screener
```

### 2. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate   # On Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a .env file in the root directory and add your API keys:
```
OPENROUTER_API_KEY=your_openrouter_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langsmith_key_here     # generate this from langsmith website
LANGCHAIN_PROJECT=resume-screening-system
```

## ▶️ Usage

### 1. Generate the dummy data (Run this once):

```
python setup_data.py
```

### 2. Run the evaluation pipeline:

```
python main.py
```
