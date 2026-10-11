from fastapi import Request, HTTPException
from repository.Lesson import LessonRepository
from repository.User import UserRepository
from schemas.lesson import LessonSchema
from schemas.completed import CompletedSchema
from repository.Completed import CompletedRepository
from auth.token_operation import decode_jwt_token
class LessonService:
    @staticmethod
    def __get_user_id_by_request(request: Request) -> int:
        token = request.cookies.get("data")
        if token is None:
            raise HTTPException(status_code=401, detail="unauthorized")
        user_id = decode_jwt_token(token)
        if not user_id or user_id.get("user_id") is None:
            raise HTTPException(status_code=401, detail="invalid token")
        return user_id["user_id"]

    @staticmethod
    def completed_lesson(lesson_id: int, request: Request):
        user_id = LessonService.__get_user_id_by_request(request)
        if CompletedRepository.is_completed(user_id = user_id, lesson_id=lesson_id):
            raise HTTPException(status_code=401, detail="lesson already completed")
        if LessonRepository.get_by_id(lesson_id) is None:
            raise HTTPException(status_code=404, detail="lesson not found")
        if UserRepository.get_by_id(user_id) is None:
            raise HTTPException(status_code=404, detail="user not found")
        lesson = LessonRepository.get_by_id(lesson_id)
        CompletedRepository.create_new(CompletedSchema(user_id=user_id, lesson_id=lesson_id))
        UserRepository.update_xp_by_id(user_id=user_id, xp=lesson.xp)
        return lesson
