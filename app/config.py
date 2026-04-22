import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "Research to Revision Assistant"
    APP_VERSION = "1.1.0"

    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")
    MISTRAL_CHAT_MODEL = os.getenv("MISTRAL_CHAT_MODEL", "mistral-small-latest")
    MISTRAL_EMBED_MODEL = os.getenv("MISTRAL_EMBED_MODEL", "mistral-embed")

    TOP_K = int(os.getenv("TOP_K", 4))
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))
    MAX_FILES_PER_UPLOAD = int(os.getenv("MAX_FILES_PER_UPLOAD", 10))
    MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", 20))

    VECTOR_DB_DIR = os.path.abspath(os.getenv("VECTOR_DB_DIR", "app/db/vector_indexes"))
    RAW_PDF_DIR = os.path.abspath(os.getenv("RAW_PDF_DIR", "data/raw_pdfs"))

settings = Settings()