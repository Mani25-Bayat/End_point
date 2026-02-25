from fastapi import FastAPI

from app.infrastructure.config.settings import settings
from app.infrastructure.http.exception_handler import register_exception_handlers
from app.interface_adapters.routers.placeholder_router import router as placeholder_router
from app.core.logger import get_logger

logger = get_logger(__name__)


def create_app() -> FastAPI:
    application = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    register_exception_handlers(application)

    application.include_router(placeholder_router, prefix="/api/v1")

    logger.info("Application started — %s v%s", settings.APP_NAME, settings.APP_VERSION)

    return application


app = create_app()
