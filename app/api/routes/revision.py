from fastapi import APIRouter
from app.schemas.revision import RevisionRequest
from app.services.revision_service import RevisionService

router = APIRouter(tags=["Revision"])
revision_service = RevisionService()

@router.post("/generate-revision-notes")
def generate_revision_notes(payload: RevisionRequest):
    return revision_service.generate_revision_notes(
        index_name=payload.index_name,
        query=payload.query,
        task=payload.task
    )