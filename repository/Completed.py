from base import Session, get_all, create_new, delete
from sqlalchemy import select
from models.completed import Completed
from schemas.completed import CompletedSchema


class CompletedRepository:

    @staticmethod
    def get_all():
        with Session() as session:
            return session.execute(select(Completed)).scalars().all()

    @staticmethod
    def create_new(compl: CompletedSchema):
        new_complited = Completed(
            user_id=compl.user_id,
            lesson_id=compl.lesson_id,
        )
        return create_new(new_complited)

    @staticmethod
    def delete_by_lesson_id_and_user_id(lesson_id: int, user_id: int):
        with Session() as session:
            obj = session.execute(
                select(Completed).where(
                    Completed.lesson_id == lesson_id,
                    Completed.user_id == user_id,
                )
            ).scalar_one_or_none()
            if obj is None:
                return None
            return delete(obj)

    @staticmethod
    def get_by_id(id):
        with Session() as session:
            return session.execute(
                select(Completed).where(Completed.id == id)
            ).scalar_one_or_none()

    @staticmethod
    def get_by_lesson_id(lesson_id):
        with Session() as session:
            return session.execute(
                select(Completed).where(Completed.lesson_id == lesson_id)
            ).scalars().all()

    @staticmethod
    def is_completed(user_id: int, lesson_id: int) -> bool:
        with Session() as session:
            obj = session.execute(
                select(Completed).where(
                    Completed.user_id == user_id,
                    Completed.lesson_id == lesson_id,
                )
            ).scalar_one_or_none()
            return obj is not None