from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Explain the constitutional text below in very simple English.
Do not give legal advice.
Limit explanation to 5 sentences.

Context:
{context}

Question:
{question}
"""
)
