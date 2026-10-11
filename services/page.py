from typing import Optional
from auth.token_operation import decode_jwt_token
from repository.Lesson import LessonRepository
from repository.User import UserRepository
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from mako.lookup import TemplateLookup
from frontend.temp.main import Template
from slowapi.errors import RateLimitExceeded

template = TemplateLookup("frontend/html/")
Templ = Template("css", "js")


class PageService:

    @staticmethod
    def _render(template_name: str,
                css_files: Optional[list[str]] = None,
                **context) -> HTMLResponse:
        css_files = css_files or ["index.css"]
        css = Templ.render_css(*css_files)
        tmpl = template.get_template(template_name)
        html = tmpl.render(css=css, **context)
        return HTMLResponse(html)

    @staticmethod
    def _get_user(request: Request):
        token = request.cookies.get("data")
        if not token:
            return None
        try:
            payload = decode_jwt_token(token)
        except Exception:
            return None
        if not isinstance(payload, dict) or payload.get("user_id") is None:
            return None
        return UserRepository.get_by_id(payload["user_id"])


    @staticmethod
    def root(request: Request) -> HTMLResponse:
        user = PageService._get_user(request)
        return PageService._render(
            "index.html",
            user_name=user.name if user else None,
            user_xp=user.xp if user else 0,
        )

    @staticmethod
    def terms(request: Request) -> HTMLResponse:
        return PageService._render(
            "terms.html",
        )

    @staticmethod
    def lessons(request: Request) -> HTMLResponse:
        user = PageService._get_user(request)
        lessons = LessonRepository.get_all()
        return PageService._render(
            "lessons.html",
            lessons=lessons,
            lessons_count=len(lessons) if lessons else 0,
            user_name=user.name if user else None,
            user_xp=user.xp if user else 0,
        )

    @staticmethod
    def lesson(request: Request, lesson_id: int) -> HTMLResponse:
        user = PageService._get_user(request)
        return PageService._render(
            "lesson.html",
            lesson=LessonRepository.get_by_id(lesson_id),
            user_name=user.name if user else None,
            user_xp=user.xp if user else 0,
        )

    @staticmethod
    def get_lesson_by_subject(request: Request, subject: str) -> HTMLResponse:
        user = PageService._get_user(request)
        lessons = LessonRepository.get_by_subject(subject)
        return PageService._render(
            "sub_lesson.html",
            lessons=lessons,
            lessons_count=len(lessons) if lessons else 0,
            user_name=user.name if user else None,
            user_xp=user.xp if user else 0,
        )

    @staticmethod
    def f429(request: Request, exc: RateLimitExceeded) -> HTMLResponse:
        user = PageService._get_user(request)

        return PageService._render(
            "f429.html",
            user_name=user.name if user else None,
            user_xp=user.xp if user else 0,
        )

    @staticmethod
    def login(request: Request) -> HTMLResponse | RedirectResponse:
        if PageService._get_user(request):
            return RedirectResponse("/", status_code=302)
        return PageService._render("login.html")

    @staticmethod
    def register(request: Request) -> HTMLResponse | RedirectResponse:
        if PageService._get_user(request):
            return RedirectResponse("/", status_code=302)
        return PageService._render("register.html")

    @staticmethod
    def me(request: Request) -> HTMLResponse | RedirectResponse:
        user = PageService._get_user(request)
        if user is None:
            return RedirectResponse("/login", status_code=302)
        return PageService._render(
            "me.html",
            username=user.name,
            user_xp=user.xp,
            user_phone=user.phone,
        )