from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from schemas.user import UserCreateSchema
from services.users_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
def create_new_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    user_service = UserService(db)

    new_user = user_service.create_user(user)

    return new_user
