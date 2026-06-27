# AI Legal Research Assistant using RAG

An AI-powered Legal Research Assistant that enables users to upload legal PDF documents and ask questions in natural language. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents before generating accurate, context-aware responses using Large Language Models.

## Features
- Upload and process legal PDF documents
- Automatic document chunking
- Semantic search using Ollama Embeddings
- FAISS Vector Database for fast retrieval
- Context-aware AI responses using Groq LLM
- Interactive Streamlit web application
- Retrieval-Augmented Generation (RAG) Pipeline

## Tech Stack
- Python
- Streamlit
- LangChain
- FAISS
- Ollama Embeddings (nomic-embed-text)
- Groq (Llama 3.3)
- PDFPlumber

## Workflow
1. Upload PDF document
2. Extract and split text into chunks
3. Generate vector embeddings
4. Store embeddings in FAISS
5. Retrieve relevant document chunks
6. Generate accurate answers using the LLM

## Future Improvements
- Multi-document support
- Chat history and memory
- Source citations
- Cloud deployment
- User authentication
