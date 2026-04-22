class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class FileValidationError(AppException):
    def __init__(self, message: str = "Invalid file uploaded"):
        super().__init__(message=message, status_code=400)


class VectorStoreError(AppException):
    def __init__(self, message: str = "Vector store operation failed"):
        super().__init__(message=message, status_code=500)


class RetrievalError(AppException):
    def __init__(self, message: str = "Failed to retrieve relevant documents"):
        super().__init__(message=message, status_code=500)


class LLMServiceError(AppException):
    def __init__(self, message: str = "LLM generation failed"):
        super().__init__(message=message, status_code=502)