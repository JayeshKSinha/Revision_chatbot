from mistralai.client import Mistral
from app.config import settings
from app.core.exceptions import LLMServiceError

class MistralClient:
    def __init__(self):
        if not settings.MISTRAL_API_KEY:
            raise LLMServiceError("Missing MISTRAL_API_KEY in environment.")
        self.client = Mistral(api_key=settings.MISTRAL_API_KEY)
        self.model = settings.MISTRAL_CHAT_MODEL

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.chat.complete(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise LLMServiceError(f"Mistral generation failed: {str(e)}")