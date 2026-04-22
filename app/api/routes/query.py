from fastapi import APIRouter
from app.schemas.query import QueryRequest
from app.dependencies import rag_pipeline

router = APIRouter(tags=["Query"])

@router.post("/ask")
def ask_question(payload: QueryRequest):
    return rag_pipeline.ask(payload.index_name, payload.query)