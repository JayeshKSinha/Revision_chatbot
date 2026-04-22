from app.services.retriever import get_relevant_docs
from app.services.mistral_client import MistralClient
from app.core.prompts import REVISION_PROMPT

class RevisionService:
    def __init__(self):
        self.llm = MistralClient()

    def generate_revision_notes(self, index_name: str, query: str, task: str):
        docs = get_relevant_docs(index_name, query)
        context = "\n\n".join(
            [
                f"Source: {doc.metadata.get('pdf_name', 'unknown')} | Page: {doc.metadata.get('page', 'NA')}\n{doc.page_content}"
                for doc in docs
            ]
        )

        prompt = REVISION_PROMPT.format(
            context=context,
            task=task,
            query=query
        )

        answer = self.llm.generate(prompt)

        return {
            "answer": answer,
            "sources": [
                {
                    "content": doc.page_content[:500],
                    "metadata": doc.metadata
                }
                for doc in docs
            ]
        }