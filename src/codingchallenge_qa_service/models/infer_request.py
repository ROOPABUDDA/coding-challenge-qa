from pydantic import BaseModel, validator
from codingchallenge_qa_service.models.qa_models import Client, Language, User

from fastapi import HTTPException


class InferRequest(BaseModel):
    query: str
    user: User
    course_id: str
    client: Client
    language: Language
    allow_annotation: bool

    @validator("query")
    def query_cannot_be_empty(cls, v):
        if v == "":
            raise HTTPException(status_code=422, detail="Query parameter can not be empty.")
        return v
