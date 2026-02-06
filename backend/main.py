from fastapi import FastAPI, Request

from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import FileResponse
import os

load_dotenv()
# app=FastAPI()
# @app.post("/explain")
# def explain_text(query: QuerySchema):
#     result = qa_chain.run(query.text)
#     return {"explanation": result}


from pypdf import PdfReader
reader=PdfReader("resources/Constitution.pdf")
number_of_pages=len(reader.pages)
page=reader.pages[1]
text=page.extract_text()
print(text)
