from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter()

TEMPLATES_DIR = Path("app/web/templates")


@router.get("/")
def login_page() -> FileResponse:
    """
    Returns the SentinelIR login page.

    Returns:
        FileResponse: The login HTML page.
    """
    return FileResponse(TEMPLATES_DIR / "login.html")
