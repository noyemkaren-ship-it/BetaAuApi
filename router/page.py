from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from starlette.responses import HTMLResponse, RedirectResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from services.page import PageService
from fastapi import APIRouter, Request

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()

@router.get("/", response_class=HTMLResponse, response_model=None)
@limiter.limit("20/minute")
async def index(request: Request) -> HTMLResponse:
    return PageService.root(request)

@router.get("/login", response_class=HTMLResponse, response_model=None)
@limiter.limit("20/minute")
async def login(request: Request) -> HTMLResponse | RedirectResponse:
    return PageService.login(request)

@router.get("/register", response_class=HTMLResponse, response_model=None)
@limiter.limit("20/minute")
async def register(request: Request) -> HTMLResponse | RedirectResponse:
    return PageService.register(request)

@router.get("/lessons", response_class=HTMLResponse, response_model=None)
@limiter.limit("20/minute")
async def lessons(request: Request) -> HTMLResponse:
    return PageService.lessons(request)

@router.get("/terms", response_class=HTMLResponse, response_model=None)
@limiter.limit("20/minute")
async def terms(request: Request) -> HTMLResponse:
    return PageService.terms(request)

@router.get("/logout")
async def logout():
    resp = RedirectResponse("/", status_code=302)
    resp.delete_cookie("data")
    return resp

@router.get("/lesson/{lesson_id}", response_class=HTMLResponse, response_model=None)
@limiter.limit("20/minute")
async def lesson(request: Request, lesson_id: int) -> HTMLResponse:
    return PageService.lesson(request,lesson_id)

@router.get("/sub/lesson/{subject}", response_class=HTMLResponse, response_model=None)
@limiter.limit("20/minute")
async def lesson_sub(request: Request, subject: str) -> HTMLResponse:
    return PageService.get_lesson_by_subject(request, subject)


@router.get("/me/page", response_class=HTMLResponse, response_model=None)
@limiter.limit("20/minute")
async def me(request: Request) -> HTMLResponse | RedirectResponse:
    return PageService.me(request)

@router.get("/me", response_class=HTMLResponse, response_model=None)
async def me_redirect():
    return RedirectResponse("/me/page")