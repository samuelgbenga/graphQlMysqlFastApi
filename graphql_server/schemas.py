
import email
from typing import Optional
import strawberry


@strawberry.type
class User:
    id: int
    name: str
    email: str
    password: str


@strawberry.input
class NewUser:
    name: str
    email: str
    password: str


@strawberry.input
class UpdateUserInfo:
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None