from base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float

class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    html_code = Column(String)
    subs = Column(Integer)
    xp = Column(Float)
    subject = Column(String)