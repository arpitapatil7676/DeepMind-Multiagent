# DeepMind – Multi-Agent AI Research System

> An AI-powered research assistant built with Streamlit, LangChain, Tavily Search, and Ollama that automatically generates structured research reports and critiques them using multiple AI stages.

---

# 🚀 Project Overview

DeepMind is a multi-stage AI research pipeline designed to automate the process of gathering information, generating reports, and evaluating report quality.

The system:

1. Searches the web for relevant information using Tavily Search
2. Collects and processes research content
3. Generates a structured research report using a local LLM
4. Reviews and critiques the generated report

The application features an interactive Streamlit interface with real-time workflow visualization.

---

# 🧠 System Workflow

## 🔍 Search Stage

Responsible for:

* Finding relevant information from the web
* Retrieving recent and reliable sources
* Gathering research data

---

## 📄 Reader Stage

Responsible for:

* Processing search results
* Organizing collected information
* Preparing content for report generation

---

## ✍️ Writer Stage

Powered by:

* Ollama
* Qwen2.5 Local LLM

Generates:

* Research reports
* Summaries
* Insights
* Structured findings

---

## 🧐 Critic Stage

Reviews:

* Report quality
* Clarity
* Completeness
* Research depth

Provides:

* Score
* Strengths
* Areas for improvement

---

# ⚡ Features

* Multi-Stage AI Research Pipeline
* Local LLM Execution using Ollama
* Tavily Web Search Integration
* Automated Report Generation
* AI-Based Report Critique
* Download Research Reports
* Interactive Streamlit Dashboard
* Modern Dark-Themed UI

---

# 🛠️ Tech Stack

## Frontend

* Streamlit
* Custom CSS
* Google Fonts

## Backend

* Python
* LangChain
* Tavily Search API
* Requests
* BeautifulSoup

## AI Components

* Ollama
* Qwen2.5:1.5B
* Prompt Engineering
* Writer Chain
* Critic Chain

---

📂 Project Structure

```bash
DeepMind/
│
├── app.py
├── agents.py
├── tools.py
├── pipeline.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/arpitapatil7676/Deepmind-multiagent.git

cd Deepmind-multiagent
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download:

https://ollama.com

Pull the model:

```bash
ollama pull qwen2.5:1.5b
```

---

## Configure Environment Variables

Create a `.env` file:

```env
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run the Application

Start Ollama:

```bash
ollama serve
```

Run Streamlit:

```bash
streamlit run app.py
```

---

# 🧪 Example Topics

* Artificial Intelligence
* Quantum Computing
* Climate Change
* Fusion Energy
* Cyber Security
* Space Exploration
* Machine Learning
* CRISPR Technology

---

# 📈 Future Improvements

* PDF Export
* Citation Support
* Multi-Source Verification
* RAG Integration
* Research History Storage
* Voice-Based Interaction
* Agent Memory
* Knowledge Graph Generation

---

# 👩‍💻 Author

Arpita Patil

GitHub:
https://github.com/arpitapatil7676
