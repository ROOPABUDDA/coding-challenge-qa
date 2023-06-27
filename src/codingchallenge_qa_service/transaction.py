import json
from codingchallenge_qa_service.logging import getLogger
from typing import Any, Dict
from uuid import uuid4

from fastapi.encoders import jsonable_encoder

logger = getLogger(name=__name__)


class Transaction:
    MAPPING = {
        "mappings": {
            "properties": {
                "request_time": {"type": "date"},
                "question": {"type": "text"},
                "query_channel": {"type": "keyword"},
                "query_channel_data": {"type": "text"},
                "student_id": {"type": "keyword"},
                "coursebook_id": {"type": "keyword"},
                "use_fallback": {"type": "boolean"},
                "is_fallback": {"type": "boolean"},
                "is_gs": {"type": "boolean"},
                "score_threshold": {"type": "float"},
                "answer": {"type": "text"},
                "score": {"type": "float"},
                "codingchallenge_qa_service_release_version": {"type": "keyword"},
                "model_approach": {"type": "keyword"},
                "model_name": {"type": "keyword"},
                "request_body": {"type": "text"},
                "response_body": {"type": "text"},
                "pipeline_steps": {"type": "text"},
                "error": {"type": "text"},
                "exc_info": {"type": "text"},
                "duration_request_total": {"type": "float"},
                "duration_preselection": {"type": "float"},
                "duration_paraphrase": {"type": "float"},
                "duration_qa": {"type": "float"},
                "duration_question_sensitive_content_detection": {"type": "float"},
                "duration_answer_sensitive_content_detection": {"type": "float"},
                "feedback": {"type": "object"},
                "thread_id": {"type": "keyword"},
                "validation": {"type": "object"},
                "transaction_id": {"type": "keyword"},
                "correlation_id": {"type": "keyword"},
                "question_sensitivity": {"type": "keyword"},
                "answer_sensitivity": {"type": "keyword"},
                "client": {"type": "object"},
                "course_id": {"type": "keyword"},
                "user": {"type": "object"},
                "question_uuid": {"type": "keyword"},
                "answer_validity": {"type": "keyword"},
                "is_gs_answer": {"type": "boolean"},
                "response_type": {"type": "keyword"},
                "language": {"type": "keyword"},
                "allow_annotation": {"type": "boolean"},
            }
        }
    }

    def __init__(self):
        self.transaction_id: str = str(uuid4())
        self.transaction_data = {}
        self.should_store = False
        self.should_update = False

    def record(self, field_update: Dict):
        """Updates the transaction nested dictionary on the first two levels.
        * If the Value is a dictionary, it doesn't replace Level 2 dictionary.
          It either replaces old values on Level 2 or creates new entries.
        * If the Value is a string, it replaces the old or creates a new entry on Level 1

        :param field_update: a dictionary contains -to be recorded- updates to the transaction data
        """
        field_update = jsonable_encoder(field_update)
        # record all pairs of updates
        for key, value in field_update.items():
            # make sure each recorded key has a type mapping
            if key not in self.MAPPING["mappings"]["properties"]:
                raise TypeError(f"{key} does not have type mapping")

            # in case of nested objects, change or add values instead of overwriting
            if isinstance(value, dict):
                for nested_key, nested_value in value.items():
                    try:
                        self.transaction_data[key][nested_key] = nested_value
                    except KeyError:
                        self.transaction_data[key] = {}
                        self.transaction_data[key][nested_key] = nested_value
            else:
                # replace old value of the key or create a new key-value pair in the transaction
                self.transaction_data[key] = value

    def to_dict(self, include_id: bool = True) -> Dict:
        """Transforming all second level dictionaries to json formatted text

        :param include_id: boolean used to include the transaction id to the transaction
        :return: a dictionary with all second level dictionaries and lists serialized as json formatted text
        """
        transaction_dict: Dict[Any, Any] = {}
        if include_id:
            transaction_dict["transaction_id"] = (self.transaction_id,)
        for key in self.transaction_data.keys():
            transaction_dict[key] = (
                self.transaction_data[key].copy()
                if callable(getattr(self.transaction_data[key], "copy", None))
                else self.transaction_data[key]
            )
            if (
                isinstance(transaction_dict[key], dict)
                and self.MAPPING["mappings"]["properties"][key]["type"] == "text"
            ):
                logger.info(f"changing type of {key}")
                transaction_dict[key] = json.dumps(transaction_dict[key])

        return transaction_dict
