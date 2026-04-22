import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from app.core.exceptions import FileValidationError

def load_pdf_documents(file_path: str):
    try:
        loader = PyPDFLoader(file_path)
        return loader.load()
    except Exception as e:
        raise FileValidationError(f"Failed to read PDF: {file_path}. Error: {str(e)}")


def load_multiple_pdf_documents(file_paths: List[str]):
    all_docs = []
    for file_path in file_paths:
        docs = load_pdf_documents(file_path)
        for doc in docs:
            doc.metadata["pdf_name"] = os.path.basename(file_path)
        all_docs.extend(docs)
    return all_docs