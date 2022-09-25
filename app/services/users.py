from sqlalchemy.orm import Session

from app.models import User
from app.utils import hash_password


def create(db: Session, username: str, password: str) -> User:
    hashed_password = hash_password(password)
    user = User(username=username, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get(db: Session, id: int) -> User:
    user = db.query(User).filter(User.id == id).first()
    return user


def get_by_username(db: Session, username: str) -> User:
    user = db.query(User).filter(User.username == username).first()
    return user
