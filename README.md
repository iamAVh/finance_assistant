# finance_assistant
# 📈 Finance Voice Assistant

A voice-activated financial assistant that answers any market-related question using real-time data from APIs (Alpha Vantage), financial news scraping (Yahoo Finance), and document retrieval via RAG (FAISS + Sentence Transformers). The agent responds with synthesized voice and text.

---

## 🛠️ Architecture Overview

```
[Voice Input (Streamlit Upload)]
            ⬇️
[STT Agent: Whisper / Faster-Whisper]
            ⬇️
[Orchestrator Agent]
   ├──> [Retriever Agent (FAISS + Embeddings)]
   ├──> [API Agent (Alpha Vantage)]
   ├──> [Scraping Agent (Yahoo Finance)]
   └──> [Language Agent (OpenAI GPT-4)]
            ⬇️
[Answer: Text + TTS Audio Output]
```

---

## 📚 Directory Structure

```
finance_manager/
├── .env
├── Dockerfile
├── requirements.txt
├── README.md
├── docs/
│   └── ai_tool_usage.md
├── data_ingestion/
│   └── ingest.py
├── agents/
│   ├── api_agent.py
│   ├── scraping_agent.py
│   ├── retriever_agent.py
│   └── language_agent.py
├── orchestrator/
│   └── orchestrator.py
├── voice_io/
│   ├── stt.py
│   └── tts.py
└── streamlit_app/
    └── app.py
```

---

## 🚀 Setup & Installation

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/finance-voice-assistant.git
cd finance-voice-assistant
```

### 2. Create `.env` file

```
OPENAI_API_KEY=your-openai-key
ALPHA_VANTAGE_API_KEY=your-alpha-vantage-key
```

### 3. Install dependencies (Python 3.10 recommended)

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit app

```bash
streamlit run streamlit_app/app.py
```

### 5. Or use Docker

```bash
docker build -t finance-agent .
docker run -p 8501:8501 finance-agent
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 🌐 Deployment (Streamlit Cloud)

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect GitHub repo
4. Set environment variables in Streamlit Cloud UI
5. Click Deploy

**Example Deployment URL**: https\://<your-name>-finance-assistant.streamlit.app

---

## 🔗 Toolkit Comparison

| Task         | Toolkit                 | Notes                             |
| ------------ | ----------------------- | --------------------------------- |
| STT          | `faster-whisper`        | Faster, lower memory than Whisper |
| TTS          | `TTS` by Coqui          | Offline, flexible voices          |
| Vector Store | `FAISS`                 | Lightweight and fast              |
| Embeddings   | `sentence-transformers` | `all-MiniLM-L6-v2` for speed      |
| LLM          | `OpenAI GPT-4`          | Reliable synthesis                |
| UI           | `Streamlit`             | Simple deployment                 |

---

## ⏳ Performance Benchmarks

| Query Type  | Avg Time  | Source         |
| ----------- | --------- | -------------- |
| STT         | \~4 sec   | Whisper        |
| API Query   | \~1.2 sec | AlphaVantage   |
| Scraping    | \~1.8 sec | Yahoo Finance  |
| FAISS + LLM | \~2.1 sec | Local + OpenAI |
| TTS Audio   | \~3 sec   | Coqui TTS      |

---


