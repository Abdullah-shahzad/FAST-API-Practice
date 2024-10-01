from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    hashed_password: str = Field(..., min_length=8)

class UserUpdate(UserBase):
    is_active: bool = True

class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
