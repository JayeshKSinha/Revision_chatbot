from langchain_mistralai import MistralAIEmbeddings
from app.config import settings

def get_embedding_model():
    return MistralAIEmbeddings(
        model=settings.MISTRAL_EMBED_MODEL,
        api_key=settings.MISTRAL_API_KEY
    )