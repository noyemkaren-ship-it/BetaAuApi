from sqlalchemy import select
from base import Base, get_all, create_new, delete, Session
from models.lesson import Lesson
from schemas.lesson import LessonSchema


class LessonRepository:

    @staticmethod
    def get_all():
        with Session() as session:
            return session.execute(
                select(Lesson).order_by(Lesson.subject.asc(), Lesson.subs.asc())
            ).scalars().all()

    @staticmethod
    def create_new(lesson: LessonSchema):
        new_lesson = Lesson(
            title=lesson.title,
            subs=lesson.subs,
            html_code=lesson.html_code,
            subject=lesson.subject,
            xp=lesson.xp,
        )
        return create_new(new_lesson)

    @staticmethod
    def delete_by_id(id: int):
        with Session() as session:
            lesson = session.execute(
                select(Lesson).where(Lesson.id == id)
            ).scalar_one_or_none()
            if lesson is None:
                return None
            return delete(lesson)

    @staticmethod
    def get_by_subject(subject: str):
        with Session() as session:
            return session.execute(
                select(Lesson)
                .where(Lesson.subject == subject)
                .order_by(Lesson.subs.asc())
            ).scalars().all()

    @staticmethod
    def get_by_id(id: int):
        with Session() as session:
            return session.execute(
                select(Lesson).where(Lesson.id == id)
            ).scalar_one_or_none()

    @staticmethod
    def get_by_title(title: str):
        with Session() as session:
            return session.execute(
                select(Lesson).where(Lesson.title == title)
            ).scalars().all()

    @staticmethod
    def get_by_html_code(html_code: str):
        with Session() as session:
            return session.execute(
                select(Lesson).where(Lesson.html_code == html_code)
            ).scalars().all()

    @staticmethod
    def get_by_subs(subs: int):
        with Session() as session:
            return session.execute(
                select(Lesson).where(Lesson.subs == subs)
            ).scalars().all()

    @staticmethod
    def get_subjects():
        from sqlalchemy import distinct
        with Session() as session:
            return [
                row[0] for row in session.execute(
                    select(distinct(Lesson.subject)).order_by(Lesson.subject)
                ).all()
                if row[0]
            ]