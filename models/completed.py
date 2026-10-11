from base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Completed(Base):
    __tablename__ = "completeds"
    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
