from app.config import settings
from app.services.vector_store import load_vector_store
from app.core.exceptions import RetrievalError

def get_relevant_docs(index_name: str, query: str):
    try:
        vector_store = load_vector_store(index_name)
        retriever = vector_store.as_retriever(search_kwargs={"k": settings.TOP_K})
        docs = retriever.invoke(query)

        if not docs:
            raise RetrievalError("No relevant documents found for the query.")

        return docs
    except RetrievalError:
        raise
    except Exception as e:
        raise RetrievalError(f"Retriever failed: {str(e)}")