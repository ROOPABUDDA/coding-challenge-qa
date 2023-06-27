from codingchallenge_qa_service.services.infer_service import InferService
from codingchallenge_qa_service.services.paraphrase_service import ParaphraseService
from codingchallenge_qa_service.services.prefiltering_service import PrefilteringService
from codingchallenge_qa_service.services.sensitive_content_detection_service import SensitiveContentDetectionService
from codingchallenge_qa_service.services.transaction_service import TransactionService


class CommonServices:
    def __init__(self):
        self.transaction_service = TransactionService()
        self.sensitive_content_detection_service = SensitiveContentDetectionService()
        self.prefiltering_service = PrefilteringService()
        self.infer_service = InferService()
        self.paraphrase_service = ParaphraseService()
