from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(UserBase):
    is_active: bool = True
    password: str = None  # Optional for updates

class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class UserModel(UserRead):
    pass
