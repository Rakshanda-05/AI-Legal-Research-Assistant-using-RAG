# ⚖️ AI Legal Research Assistant using RAG

An AI-powered Legal Research Assistant that enables users to upload legal PDF documents and ask natural language questions. The application leverages Retrieval-Augmented Generation (RAG) to retrieve the most relevant legal information from uploaded documents and generate accurate, context-aware responses using Large Language Models.

---

## 🚀 Features

- 📄 Upload and analyze legal PDF documents
- 🔍 Semantic document search using vector embeddings
- 🧩 Automatic document chunking and indexing
- 🤖 AI-powered legal question answering
- ⚖️ Structured responses with:
  - Relevant Articles
  - Legal Analysis
  - Reasoning
  - Final Conclusion
  - Confidence Score
- 💬 Interactive Streamlit-based chat interface
- ⚡ Fast inference using Groq Llama 3.3

---

## 🏗️ System Architecture

```
PDF Upload
      │
      ▼
PDF Loader (PDFPlumber)
      │
      ▼
Text Chunking
(RecursiveCharacterTextSplitter)
      │
      ▼
Embeddings
(Ollama - nomic-embed-text)
      │
      ▼
FAISS Vector Store
      │
      ▼
Semantic Retrieval
      │
      ▼
Groq Llama 3.3
      │
      ▼
Context-Aware AI Response
```

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Frontend
- Streamlit

### AI Framework
- LangChain

### Vector Database
- FAISS

### Embedding Model
- Ollama (`nomic-embed-text`)

### Large Language Model
- Groq API (`llama-3.3-70b-versatile`)

### Document Processing
- PDFPlumber

---

## 📂 Project Structure

```text
AI-Legal-Research-Assistant-using-RAG/
│
├── Frontend.py              # Streamlit UI
├── rag_pipeline.py          # RAG Pipeline
├── vector_database.py       # PDF Processing & FAISS
├── requirements.txt
├── README.md
├── .env.example
├── pdf/
├── vectorstore/
└── images/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Legal-Research-Assistant-using-RAG.git
cd AI-Legal-Research-Assistant-using-RAG
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama from:

https://ollama.com/download

### Pull Required Models

```bash
ollama pull deepseek-r1
ollama pull nomic-embed-text
```

### Start Ollama

```bash
ollama serve
```

### Configure Environment Variables

Create a `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
```

### Run the Application

```bash
streamlit run Frontend.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📸 Screenshots

Add screenshots of:

- Home Screen
- PDF Upload
- AI Chat Interface
- Legal Analysis Response

---

## 🎥 Demo Video

(Add your YouTube or Google Drive demo link here.)

---

## 🔮 Future Enhancements

- Multi-document support
- Conversation memory
- Citation highlighting
- OCR support for scanned PDFs
- Legal document summarization
- Case law recommendation system

---

## 👩‍💻 Author

**Rakshanda Talwekar**

- LinkedIn: https://www.linkedin.com/in/rakshanda05
- GitHub: https://github.com/Rakshanda-05
