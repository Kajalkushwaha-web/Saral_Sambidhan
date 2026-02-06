from loader import load_document
from splitter import split_and_chunking
from documents import create_documents
from embeddings import get_embeddings
from vectorstore import create_vector_index, save_vector_index

from pathlib import Path


PDF_PATH="resources/Constitution.pdf"
def ingest():
    print("Loading PDF document.....")
    text=load_document(PDF_PATH)

    print("Splitting text .....")
    chunks=split_and_chunking(text)
    
    print("Creating Documents ....")
    documents=create_documents(chunks)

    print("Generating embeddings + FAISS index ...")
    embeddings=get_embeddings()
    vectorstore=create_vector_index(documents,embeddings)

    save_vector_index(vectorstore)

    print("Ingestion Complete")

if __name__=="__main__":
    ingest()
