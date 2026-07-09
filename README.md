# 🧠 Research Mind

**Research Mind** is a Multi-Agent AI Research Assistant that automates the process of researching, extracting, summarizing, and generating structured reports from real-time web data.

Built using **LangGraph**, **LangChain**, **Groq LLM**, **Tavily Search**, and **Streamlit**, the application follows a modular multi-agent workflow to produce concise research reports with a modern user interface.

---

## 🚀 Features

- Multi-Agent AI Workflow
- AI-powered Research Planning
- Real-time Web Search using Tavily
- Intelligent Information Extraction
- AI-based Summarization
- Professional Research Report Generation
- Download Report as PDF
- Interactive Streamlit Web Interface
- Clean Modular Project Structure

---

## 🛠️ Technologies Used

- Python
- LangChain
- LangGraph
- Groq LLM
- Tavily Search API
- Streamlit
- ReportLab
- python-dotenv

---

## 📂 Project Structure

```
Research Mind
│
├── app
│   ├── agents
│   │   ├── planner.py
│   │   ├── search.py
│   │   ├── extractor.py
│   │   ├── summarizer.py
│   │   └── writer.py
│   │
│   ├── graph
│   │   ├── state.py
│   │   └── workflow.py
│   │
│   ├── tools
│   │   ├── search_tool.py
│   │   └── pdf_export.py
│   │
│   ├── ui
│   │   ├── streamlit_app.py
│   │   └── styles.css
│   │
│   ├── config.py
│   └── llm.py
│
├── reports
├── data
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/Research-Mind.git
```

Navigate to the project

```bash
cd Research-Mind
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run the Application

```bash
python -m streamlit run app/ui/streamlit_app.py
```

---

## 🧩 Multi-Agent Workflow

```
User
   │
   ▼
Planner Agent
   │
   ▼
Search Agent
   │
   ▼
Extractor Agent
   │
   ▼
Summarizer Agent
   │
   ▼
Writer Agent
   │
   ▼
Final Research Report
```

---

## 📄 Output

The application generates:

- Structured Research Report
- AI-generated Summary
- Downloadable PDF Report

---

## 🎯 Future Improvements

- Chat with Generated Reports
- Multiple LLM Support
- Research History
- Dark/Light Theme Toggle

---

## 👨‍💻 Developed By

**Nithi**

---

## 📜 License

This project is developed for educational and portfolio purposes.


## 📸 Screenshots

### 🏠 Home Page

![Home](assets/home.png)

---

### 📄 Research Report - AI in Healthcare

![Report 1](assets/report1.png)

---

### 📄 Research Report - Artificial Intelligence in Education

![Report 2](assets/report2.png)

---

### 📄 Research Report - Cybersecurity Trends

![Report 3](assets/report3.png)
