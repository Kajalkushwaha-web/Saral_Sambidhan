from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from embeddings import get_embeddings
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""

    "Hina, Paste the prompt here "

Context:
{context}

Question:
{question}
"""
)
