from codingchallenge_qa_service.logging import getLogger
from typing import Any, Dict
from random import randint

logger = getLogger(name=__name__)


class SensitiveContentDetectionService:
    """Service for checking queries for sensitive content."""

    async def run(self, query: str, user_id: str) -> Dict[str, Any]:
        if randint(0, 1) == 0:
            logger.warn("Sensitive content detected")
            return {"sensitivity": "UNSAFE", "model_name": "SCD_MODEL"}

        return {"sensitivity": "SAFE", "model_name": "SCD_MODEL"}
