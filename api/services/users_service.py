from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserCreateSchema


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreateSchema):
        db_user = User(username=user.username, password=user.password, email=user.email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
