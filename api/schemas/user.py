from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    username: str


class UserCreateSchema(UserBaseSchema):
    email: EmailStr | None = None
    password: str


class UserSchema(UserBaseSchema):
    id: int
    email: EmailStr | None = None

    class Config:
        from_attributes = True
