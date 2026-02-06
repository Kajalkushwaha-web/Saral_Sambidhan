from langchain.vectorstores import FAISS

vectorstore=FAISS.from_documents(
    documents=docs,
    embedding=embeddings
)

vectorstore.save_local("faiss_index")