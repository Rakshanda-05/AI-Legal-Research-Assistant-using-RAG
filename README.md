# AI Legal Research Assistant using RAG

## Overview

The AI Legal Research Assistant is a Retrieval-Augmented Generation (RAG) application that enables users to upload legal PDF documents and ask questions in natural language. The system extracts relevant information from uploaded documents using semantic search and generates context-aware answers using a Large Language Model (LLM).

This project demonstrates practical implementation of document retrieval, embeddings, vector databases, and Generative AI for intelligent document question answering.

---

## Features

* Upload and process legal PDF documents
* Automatic PDF text extraction
* Intelligent document chunking
* Semantic search using Ollama Embeddings (`nomic-embed-text`)
* FAISS Vector Database for efficient similarity search
* Context-aware AI responses using Groq Llama 3.3
* Interactive Streamlit web interface
* Retrieval-Augmented Generation (RAG) pipeline

---

## Tech Stack

* Python
* Streamlit
* LangChain
* LangChain Community
* FAISS
* Ollama Embeddings (`nomic-embed-text`)
* Groq API (Llama 3.3-70B Versatile)
* PDFPlumber

---

## Project Workflow

1. Upload a legal PDF document.
2. Extract text using PDFPlumber.
3. Split the document into overlapping chunks.
4. Generate embeddings using Ollama (`nomic-embed-text`).
5. Store embeddings in a FAISS vector database.
6. Retrieve the most relevant document chunks for the user's query.
7. Generate a context-aware answer using Groq Llama 3.3.

---

## Project Architecture

```text
PDF Upload
     │
     ▼
PDFPlumber
     │
     ▼
Document Chunking
     │
     ▼
Ollama Embeddings (nomic-embed-text)
     │
     ▼
FAISS Vector Database
     │
     ▼
Similarity Search
     │
     ▼
Groq Llama 3.3
     │
     ▼
AI Response
```

---

## Future Improvements

* Support for multiple PDF documents
* Chat history and conversational memory
* Source citations for generated responses
* OCR support for scanned PDFs
* Cloud deployment
* User authentication

---

## Author

**Rakshanda Takwekar**

AI • Data Science • Machine Learning • Generative AI
