from pydantic import BaseModel
from uuid import UUID


class InferResponse(BaseModel):
    answer: str
    question: str
    answer_validity: str
    is_gs_answer: bool
    question_uuid: UUID
    transaction_id: UUID
