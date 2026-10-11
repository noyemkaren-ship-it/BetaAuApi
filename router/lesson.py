from fastapi import APIRouter, Request
from services.lesson import LessonService

router = APIRouter(tags=['Lesson'])

@router.post("/lesson/completed/{lesson_id}")
async def completed_lesson(lesson_id: int, request: Request):
    return LessonService.completed_lesson(lesson_id, request)