from base import Session, get_all, create_new, delete
from models.user import User
from auth.hesh_password import hesh_password
from utils.other.profanity_chaker import profanity_checker


class UserRepository:

    @staticmethod
    def get_all():
        return get_all(User)

    @staticmethod
    def get_by_id(user_id: int) -> User:
        with Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            return user

    @staticmethod
    def get_by_username(name: str) -> User:
        with Session() as session:
            user = session.query(User).filter(User.name == name).first()
            return user

    @staticmethod
    def create(name: str, password: str, email: str, phone: str, is_admin: bool = False) -> User:
        if profanity_checker(name):
            raise "profanity words in name"
        if UserRepository.get_by_username(name) is not None:
            raise "Username already in use"
        with Session() as session:
            user = User(name=name, email=email, phone=phone, is_admin=is_admin, hesh_password=hesh_password(password))
            session.add(user)
            session.commit()
            return user

    @staticmethod
    def update_xp_by_id(user_id: int, xp: float):
        with Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user is None:
                return None
            user.xp += xp
            session.commit()
            return user


    @staticmethod
    def get_by_name_and_password(name: str, password: str) -> User:
        with Session() as session:
            user = session.query(User).filter(User.name == name, User.hesh_password == hesh_password(password)).first()
            return user

    @staticmethod
    def delete_by_name(name: str):
        return delete(UserRepository.get_by_username(name))

    @staticmethod
    def is_admin(name: str) -> bool:
        with Session() as session:
            user = session.query(User).filter(User.name == name).first()
            return user.is_admin