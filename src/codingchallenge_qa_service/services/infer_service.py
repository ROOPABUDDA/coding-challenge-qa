from codingchallenge_qa_service.logging import getLogger
from typing import Any, Dict

logger = getLogger(name=__name__)


class InferService:
    """
    Service for inferring an answer

    ...

    Methods
    -------
    run(query: str)
    executes a query
    """

    async def run(self, query: str, doc: Dict, user_id: str, language: str) -> Dict[str, Any]:

        return {
            "answer": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium",  # noqa: E501
            "doc_id": "0000",
            "model_context": {"model_name": "INFER_MODEL_NAME"},
        }

    @staticmethod
    def _postprocessing_openai_prompt(raw_answer: str, language: str) -> str:
        return raw_answer + " (proccessed)"
