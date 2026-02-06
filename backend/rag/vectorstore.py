from langchain_community.vectorstores import FAISS

#creating faiss index
def create_vector_index(documents,embeddings):
    vectorstore=FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )
    return vectorstore

#saving vector embeddings
def save_vector_index(vectorstore,path="faiss_index"):
    vectorstore.save_local(path)
