from pydantic import BaseModel

class QueryRequest(BaseModel):
    index_name: str
    query: str