# ⚖️ AI Legal Research Assistant using RAG

An AI-powered Legal Research Assistant that enables users to upload legal PDF documents and ask natural language questions. The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant legal content and generate context-aware responses using Large Language Models.

---

## 🚀 Features

- Upload legal PDF documents
- Automatic document chunking and indexing
- Semantic search using vector embeddings
- Context-aware question answering
- Interactive Streamlit interface
- Fast AI responses powered by Groq Llama 3.3

---

## 🏗️ System Architecture

PDF Upload
↓
Text Extraction
↓
Text Chunking
↓
Vector Embeddings (Ollama - nomic-embed-text)
↓
ChromaDB Vector Store
↓
Semantic Retrieval
↓
Groq Llama 3.3
↓
AI Response

---

## 🛠️ Tech Stack

### Programming
- Python

### Frameworks
- Streamlit
- LangChain

### Vector Database
- ChromaDB

### Embedding Model
- Ollama (nomic-embed-text)

### Large Language Model
- Groq API (Llama 3.3)

---

## 📂 Project Structure

```
AI-Legal-Research-Assistant/
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
├── chroma_db/
├── data/
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Rakshanda-05/AI-Legal-Research-Assistant-using-RAG.git

cd AI-Legal-Research-Assistant-using-RAG

pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

## 📌 Workflow

1. Upload a legal PDF.
2. Extract text from the document.
3. Split text into chunks.
4. Generate vector embeddings.
5. Store embeddings in ChromaDB.
6. Retrieve the most relevant chunks.
7. Generate an AI response using Groq Llama 3.3.

---

## 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- LangChain
- Prompt Engineering
- Streamlit
- Document Processing
- AI Application Development

---

## 🔮 Future Improvements

- Multi-PDF support
- Citation generation
- Chat history
- OCR for scanned PDFs
- User authentication

---

## 👩‍💻 Author

Rakshanda Talwekar

LinkedIn: https://linkedin.com/in/rakshanda05
