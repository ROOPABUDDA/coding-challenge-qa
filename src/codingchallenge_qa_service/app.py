from fastapi import FastAPI

from codingchallenge_qa_service._version import __version__
from codingchallenge_qa_service.middlewares.transaction_middleware import TransactionMiddleware
from codingchallenge_qa_service.routers import infer
from codingchallenge_qa_service.routers import health
from codingchallenge_qa_service.services.common_services import CommonServices
from codingchallenge_qa_service.logging import getLogger

logger = getLogger(__name__)


def create_app() -> FastAPI:

    app = FastAPI(name="codingchallenge_qa_service", version=__version__)

    """
    Add Routers
    """
    logger.info("registering route handlers")
    app.include_router(health.router)
    app.include_router(infer.router)

    """
    Add Common Services
    """
    logger.info("[APP] registering common services")
    app.state.services = CommonServices()

    """
    Add Middleware Layers (First In Last Out)
    """
    logger.info("registering middlewares")
    app.add_middleware(TransactionMiddleware)

    logger.info("[APP] ready for liftoff 🚀")
    return app
