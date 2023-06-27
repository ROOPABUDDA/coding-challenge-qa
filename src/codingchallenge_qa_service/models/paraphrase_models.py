from typing import Any, Dict
from uuid import UUID

from pydantic import BaseModel


class ParaphraseServiceRequest(BaseModel):
    question_content_str: str
    course_id: str


class ParaphraseServiceResponse(BaseModel):
    question_origin_uuid: UUID
    question_origin_content_str: str
    course_id: str
    gs_answer_uuid: UUID
    gs_answer_content_str: str
    meta_data: Dict[str, Any]
