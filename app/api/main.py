from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routers.pages import router as pages_router


def create_app() -> FastAPI:
    """
    Creates and configures the SentinelIR FastAPI application.

    Returns:
        FastAPI: Configured FastAPI application instance.
    """
    application = FastAPI(
        title="SentinelIR",
        description="SentinelIR Web API",
    )

    application.mount(
        "/static",
        StaticFiles(directory="app/web/static"),
        name="static",
    )

    application.include_router(pages_router)

    return application


app = create_app()
