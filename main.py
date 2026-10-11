import uvicorn
from fastapi import FastAPI, Request
from dotenv import load_dotenv
load_dotenv()
from base import engine, Base
from models import *
from router import *
from services.page import PageService
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

limiter = Limiter(key_func=get_remote_address, default_limits=["20/minute"])

app = FastAPI(title="Betta")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, PageService.f429)
app.add_middleware(SlowAPIMiddleware)
app.include_router(user_router)
app.include_router(page_router)
app.include_router(lesson_router)

if __name__ == "__main__":
    try:
        Base.metadata.create_all(engine)
        uvicorn.run("main:app", port=3500, reload=True, host="0.0.0.0")
    except Exception as e:
        print(f"Error {e}")
