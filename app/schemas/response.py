from pydantic import BaseModel
from typing import List, Dict, Any

class SourceItem(BaseModel):
    content: str
    metadata: Dict[str, Any]

class APIResponse(BaseModel):
    answer: str
    sources: List[SourceItem]