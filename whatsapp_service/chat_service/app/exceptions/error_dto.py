from pydantic import BaseModel

class ErrorResponseDTO(BaseModel):
    detail: str
    status_code: int
