from pydantic import BaseModel

class RevisionRequest(BaseModel):
    index_name: str
    query: str
    task: str = "Generate concise revision notes from the retrieved research context."