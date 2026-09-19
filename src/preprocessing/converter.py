import os
from pypdf import PdfReader
from docx import Document
import re


def file_loader(folder_path):
    documents=[]
    doc_id=0

    for filename in sorted(os.listdir(folder_path)):
        ext=os.path.splitext(filename)[1].lower()
        full_path=os.path.join(folder_path, filename)


        if not os.path.isfile(full_path):
            continue
        text=""
        if(ext==".txt"):
            text=read_txt(full_path)
        elif(ext==".pdf"):
            text=read_pdf(full_path)
        elif(ext==".docx"):
            text=read_docx(full_path)
        else:
            continue

        if not text.strip():
            # print("no text found in:", filename)
            continue

        documents.append({
            "id": doc_id,
            "filename": filename,
            "text": text,
        })

        doc_id+=1

    return documents

def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf(path):
    reader = PdfReader(path)
    pages_text = []
    for page in reader.pages:
        pages_text.append(page.extract_text())
    return "\n".join(pages_text)


def read_docx(path):
    doc = Document(path)
    paragraphs_text = []
    for paragraph in doc.paragraphs:
        paragraphs_text.append(paragraph.text)
    return "\n".join(paragraphs_text)
