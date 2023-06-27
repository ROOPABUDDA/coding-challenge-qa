from codingchallenge_qa_service.logging import getLogger
from typing import Optional
from uuid import uuid4
from random import randint

from codingchallenge_qa_service.models.paraphrase_models import ParaphraseServiceRequest, ParaphraseServiceResponse

logger = getLogger(name=__name__)


class ParaphraseService:
    async def find_paraphrase(
        self, request_body: ParaphraseServiceRequest
    ) -> Optional[ParaphraseServiceResponse]:

        if randint(0, 1) == 0:
            logger.info("No paraphrase found")
            return None

        return {
            "paraphrase_service_response": ParaphraseServiceResponse(
                question_origin_uuid=uuid4(),
                question_origin_content_str="Et harum quidem rerum facilis est et expedita distinctio",
                course_id="0000-0000-0",
                gs_answer_uuid=uuid4(),
                gs_answer_content_str="Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem",  # noqa: E501
                meta_data={
                    "coursebook_ids": ["0000-0000-0"],
                    "language": "de"
                },
            )}
