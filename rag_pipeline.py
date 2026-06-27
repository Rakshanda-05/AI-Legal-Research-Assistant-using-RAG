from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from vector_database import faiss_db

# Step 1: Load environment variables
load_dotenv()

# Step 2: Setup LLM
llm_model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# Step 3: Retrieve documents
def retrieve_docs(query):
    return faiss_db.similarity_search(query)


def get_context(documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    return context


# Step 4: Prompt Template
custom_prompt_template = """
You are an AI Legal Research Assistant.

Answer ONLY using the provided context.

If the answer is unavailable in the context, say:
"I couldn't find this information in the uploaded document."

For every answer provide the following sections:

1. Relevant Articles
2. Legal Analysis
3. Reasoning
4. Final Conclusion
5. Confidence Score (0-100%)

Question:
{question}

Context:
{context}
"""

# Step 5: Generate answer
def answer_query(documents, model, query):
    context = get_context(documents)

    prompt = ChatPromptTemplate.from_template(custom_prompt_template)

    chain = prompt | model

    response = chain.invoke({
        "question": query,
        "context": context
    })

    return response.content


# Step 6: Ask Question
# question = "If a government forbids the right to assemble peacefully which articles are violated and why?"
# retrieved_docs = retrieve_docs(question)
# print("AI Lawyer:", answer_query(retrieved_docs, llm_model, question))