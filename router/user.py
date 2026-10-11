from fastapi import APIRouter, Request, Response
from slowapi import Limiter
from slowapi.util import get_remote_address
from schemas.user import User, UserLogin
from services.user import UserService

router = APIRouter(tags=["users"], prefix="/user")
limiter = Limiter(key_func=get_remote_address)

@router.post("/register")
@limiter.limit("20/minute")
async def register(request: Request, response: Response, user: User):
    return UserService.register(response, user)

@router.post("/login")
@limiter.limit("20/minute")
async def login(request: Request, response: Response, user: UserLogin):
    return UserService.login(response, user)

@router.get("/admin/users")
async def admin_users(request: Request):
    return UserService.get_all(request)

@router.get("/me")
async def me(request: Request):
    return UserService.me(request)
