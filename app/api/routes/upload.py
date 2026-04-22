from typing import List
from fastapi import APIRouter, UploadFile, File
from app.utils.file_utils import save_multiple_files
from app.utils.id_generator import generate_index_name
from app.services.pdf_loader import load_multiple_pdf_documents
from app.services.text_splitter import split_documents
from app.services.vector_store import create_and_save_vector_store

router = APIRouter(tags=["Upload"])

@router.post("/upload-pdfs")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    saved_paths = save_multiple_files(files)
    documents = load_multiple_pdf_documents(saved_paths)
    chunks = split_documents(documents)

    index_name = generate_index_name(files[0].filename)
    create_and_save_vector_store(chunks, index_name)

    uploaded_files = [file.filename for file in files]

    return {
        "success": True,
        "message": "PDFs uploaded and indexed successfully.",
        "index_name": index_name,
        "uploaded_files": uploaded_files,
        "documents_loaded": len(documents),
        "chunks_created": len(chunks)
    }