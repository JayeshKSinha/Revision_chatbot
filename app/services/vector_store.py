import os
from langchain_community.vectorstores import FAISS
from app.services.embeddings import get_embedding_model
from app.config import settings
from app.core.exceptions import VectorStoreError

def create_and_save_vector_store(chunks, index_name: str):
    try:
        embeddings = get_embedding_model()
        vector_store = FAISS.from_documents(chunks, embeddings)
        save_path = os.path.join(settings.VECTOR_DB_DIR, index_name)
        os.makedirs(save_path, exist_ok=True)
        vector_store.save_local(save_path)
        return save_path
    except Exception as e:
        raise VectorStoreError(f"Failed to create vector store: {str(e)}")


def load_vector_store(index_name: str):
    try:
        embeddings = get_embedding_model()
        load_path = os.path.join(settings.VECTOR_DB_DIR, index_name)

        if not os.path.exists(load_path):
            raise VectorStoreError(f"Index '{index_name}' not found.")

        return FAISS.load_local(
            load_path,
            embeddings,
            allow_dangerous_deserialization=True
        )
    except VectorStoreError:
        raise
    except Exception as e:
        raise VectorStoreError(f"Failed to load vector store: {str(e)}")