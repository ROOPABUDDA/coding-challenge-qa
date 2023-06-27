from codingchallenge_qa_service.logging import getLogger
from typing import Awaitable, Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from codingchallenge_qa_service._version import __version__
from codingchallenge_qa_service.transaction import Transaction
from codingchallenge_qa_service.measure import Clock, Measure

logger = getLogger(name=__name__)


class TransactionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        time_request: Clock = Measure.start_clock()

        request.state.transaction = Transaction()

        response = await call_next(request)

        duration = time_request.stop()

        if request.state.transaction.should_store:
            request.state.transaction.record(
                {
                    "request_time": Measure.current_time(),
                    "duration_request_total": duration,
                    "transaction_id": request.state.transaction.transaction_id,
                    "codingchallenge_qa_service_release_version": __version__,
                }
            )
            try:
                request.app.state.services.transaction_service.create(request.state.transaction)
                logger.info(
                    "[Transaction_Middleware] Transaction created: " f"'{request.state.transaction.transaction_id}'",
                    extra={"context": request.state.transaction.transaction_data},
                )
            except Exception as e:
                logger.error(
                    "[Transaction_Middleware] exception thrown in create transaction",
                    exc_info=e,
                )
        if request.state.transaction.should_update:
            try:
                request.app.state.services.transaction_service.update(request.state.transaction)
                logger.debug(
                    "[Transaction_Middleware] Transaction updated: " f"'{request.state.transaction.transaction_id}'"
                )
            except Exception as e:
                logger.error(
                    "[Transaction_Middleware] exception thrown in update transaction",
                    exc_info=e,
                )

        return response
