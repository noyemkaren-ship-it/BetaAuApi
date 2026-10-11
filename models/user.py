from sqlalchemy import Column, String, Integer, Float, Boolean
from base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    hesh_password = Column(String, nullable=False)
    xp = Column(Float, nullable=False, default=0.0)
    is_admin = Column(Boolean, nullable=False, default=False)

