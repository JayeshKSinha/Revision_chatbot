import os
import shutil
from typing import List
from fastapi import UploadFile
from app.config import settings
from app.core.exceptions import FileValidationError

ALLOWED_EXTENSIONS = {".pdf"}


def validate_file(upload_file: UploadFile):
    if not upload_file.filename:
        raise FileValidationError("Uploaded file must have a filename.")

    ext = os.path.splitext(upload_file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise FileValidationError(f"Unsupported file type: {upload_file.filename}")

    content_type = upload_file.content_type or ""
    if "pdf" not in content_type and not upload_file.filename.lower().endswith(".pdf"):
        raise FileValidationError(f"File is not a valid PDF: {upload_file.filename}")


def save_uploaded_file(upload_file: UploadFile) -> str:
    validate_file(upload_file)

    os.makedirs(settings.RAW_PDF_DIR, exist_ok=True)
    file_path = os.path.join(settings.RAW_PDF_DIR, upload_file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return file_path


def save_multiple_files(files: List[UploadFile]) -> List[str]:
    if not files:
        raise FileValidationError("No files were uploaded.")

    if len(files) > settings.MAX_FILES_PER_UPLOAD:
        raise FileValidationError(
            f"Maximum {settings.MAX_FILES_PER_UPLOAD} files allowed per upload."
        )

    saved_paths = []
    for file in files:
        saved_paths.append(save_uploaded_file(file))

    return saved_paths