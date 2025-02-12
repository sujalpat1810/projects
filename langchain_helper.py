import os
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import PyPDF2 as pdf

load_dotenv()

sec_key = os.getenv("HF_TOKEN")


def get_llm_response(input):
    repo_id="mistralai/Mistral-7B-Instruct-v0.2"
    llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=128,temperature=0.7,token=sec_key)
    response = llm.invoke(input)
    return response


def input_pdf_to_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text