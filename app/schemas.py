from datetime import datetime

from pydantic import BaseModel, HttpUrl


class BaseResponse(BaseModel):
    msg: str = ""
    err: str | list = ""
    data: dict | list = {}


# URL
class NewUrlRequest(BaseModel):
    original: HttpUrl


class Url(NewUrlRequest):
    alias: str

    class Config:
        orm_mode = True


class UrlResponse(BaseResponse):
    data: Url


class UrlsResponse(BaseResponse):
    data: list[Url]


# User
class BaseUser(BaseModel):
    username: str


class NewUserRequest(BaseUser):
    password: str


class LoginRequest(NewUserRequest):
    pass


class User(BaseUser):
    create_time: datetime

    class Config:
        orm_mode = True


class UserResponse(BaseResponse):
    data: User


# Token
class BaseToken(BaseModel):
    token_type: str = "Bearer"
    access_token: str


class TokenPayload(BaseModel):
    sub: int


class TokenResponse(BaseResponse):
    data: BaseToken
