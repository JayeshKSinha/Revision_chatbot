from app.services.retriever import get_relevant_docs
from app.services.mistral_client import MistralClient
from app.core.prompts import QA_PROMPT

class RAGPipeline:
    def __init__(self):
        self.llm = MistralClient()

    def ask(self, index_name: str, query: str):
        docs = get_relevant_docs(index_name, query)
        context = "\n\n".join(
            [
                f"Source: {doc.metadata.get('pdf_name', 'unknown')} | Page: {doc.metadata.get('page', 'NA')}\n{doc.page_content}"
                for doc in docs
            ]
        )

        prompt = QA_PROMPT.format(
            context=context,
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