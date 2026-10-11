from auth.token_operation import decode_jwt_token, create_jwt_token
from repository.User import UserRepository
from utils.other.profanity_chaker import profanity_checker
from schemas.user import User as UserSchema, UserLogin
from fastapi import Response, HTTPException, Request


class UserService:

    @staticmethod
    def register(response: Response, user: UserSchema):
        if (
            profanity_checker(user.name)
            or profanity_checker(user.email)
            or "@" not in user.email
            or UserRepository.get_by_username(user.name) is not None
        ):
            raise HTTPException(status_code=409, detail="conflict")

        UserRepository.create(
            name=user.name,
            email=user.email,
            password=user.password,
            phone=user.phone,
            is_admin=False,
        )
        user_data = UserRepository.get_by_username(user.name)
        information = {"user_id": user_data.id}
        response.set_cookie(key="data", value=create_jwt_token(data=information))
        return {"status_code": 201, "detail": "user registered"}

    @staticmethod
    def login(response: Response, user: UserLogin):
        user_data = UserRepository.get_by_name_and_password(
            name=user.name, password=user.password
        )
        if user_data is not None:
            response.set_cookie(
                key="data", value=create_jwt_token(data={"user_id": user_data.id})
            )
            return {"status_code": 200, "detail": "user logged in"}
        raise HTTPException(status_code=404, detail="user not found")

    @staticmethod
    def get_all(request: Request):
        token = request.cookies.get("data")
        if token is None:
            raise HTTPException(status_code=401, detail="unauthorized")

        user_id = decode_jwt_token(token)
        if not user_id or user_id.get("user_id") is None:
            raise HTTPException(status_code=401, detail="invalid token")

        user = UserRepository.get_by_id(user_id["user_id"])
        if user is None:
            raise HTTPException(status_code=404, detail="user not found")

        if user.is_admin:
            return UserRepository.get_all()
        raise HTTPException(status_code=403, detail="forbidden")

    @staticmethod
    def get_user_xp(request: Request):
        token = request.cookies.get("data")
        if token is None:
            raise HTTPException(status_code=401, detail="unauthorized")
        user_id = decode_jwt_token(token)
        if not user_id or user_id.get("user_id") is None:
            raise HTTPException(status_code=401, detail="invalid token")
        user = UserRepository.get_by_id(user_id["user_id"])
        if user is None:
            raise HTTPException(status_code=404, detail="user not found")
        return user.xp

    @staticmethod
    def get_user_name(request: Request):
        token = request.cookies.get("data")
        if token is None:
            raise HTTPException(status_code=401, detail="unauthorized")
        user_id = decode_jwt_token(token)
        if not user_id or user_id.get("user_id") is None:
            raise HTTPException(status_code=401, detail="invalid token")
        user = UserRepository.get_by_id(user_id["user_id"])
        if user is None:
            raise HTTPException(status_code=404, detail="user not found")
        return user.name


    @staticmethod
    def me(request: Request):
        token = request.cookies.get("data")
        if token is None:
            raise HTTPException(status_code=401, detail="unauthorized")
        user_id = decode_jwt_token(token)
        if not user_id or user_id.get("user_id") is None:
            raise HTTPException(status_code=401, detail="invalid token")
        user = UserRepository.get_by_id(user_id["user_id"])
        if user is None:
            raise HTTPException(status_code=404, detail="user not found")
        return user.name, user.email, user.phone, user.xp, user.is_admin