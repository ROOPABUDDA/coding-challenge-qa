from codingchallenge_qa_service.logging import getLogger
from typing import Dict, List, Optional

from codingchallenge_qa_service.models.qa_models import Language

logger = getLogger(name=__name__)


class PrefilteringService:
    """Service for pre filtering documents"""

    async def run(self, query: str, language: Language, coursebook_ids: Optional[List[str]] = None) -> Dict:
        return {
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  # noqa: E501
            "doc_id": "0000-0000-0",
            "meta": {
                "coursebook_ids": coursebook_ids,
                "language": language
            },
        }
