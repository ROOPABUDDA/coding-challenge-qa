from codingchallenge_qa_service.logging import getLogger

from codingchallenge_qa_service.transaction import Transaction


logger = getLogger(__name__)


class TransactionService:
    """
    Handles the storage and updating of transactions

    Methods
    -------
    create(transaction: Transaction)
    Stores a transaction
    update(transaction: Transaction)
    Updates a transaction
    """

    def create(self, transaction: Transaction):
        logger.debug(f"CREATE transaction: '{transaction.transaction_id}'", extra={
            "transaction_data": transaction.to_dict(include_id=False)
        })

    def update(self, transaction: Transaction):
        logger.debug(f"UPDATE transaction: '{transaction.transaction_id}'", extra={
            "transaction_data": transaction.to_dict(include_id=False)
        })
