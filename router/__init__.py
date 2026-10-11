from .lesson import router as lesson_router
from .user import router as user_router
from .page import router as page_router

__all__ = [
    "lesson_router",
    "user_router",
    "page_router"
]