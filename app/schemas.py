from pydantic import BaseModel, EmailStr, StringConstraints,Field
from typing import Optional
from datetime import datetime
from typing_extensions import Annotated



# ---------------- POSTS ----------------

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id:int
    owner:UserOut

    class Config:
        from_attributes = True   # Pydantic v2

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        from_attributes = True   # Pydantic v2



# ---------------- USERS ----------------

class UserCreate(BaseModel):
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8)]
    





class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True



class Token(BaseModel):
    access_toke:str
    token_type:str

class TokenData(BaseModel):
    id: Optional[int] = None




#-----------------------------VOTE-----------------------------

class Vote(BaseModel):
    post_id:int
    dir: Annotated[int, Field(ge=0, le=1)]

