from sqlalchemy.orm import Session
from nanoid import generate

from app.models import Url


def create(db: Session, user_id: int, original: str) -> Url:
    alias = generate(size=10)
    url = Url(user_id=user_id, original=original, alias=alias)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url


def get(db: Session, user_id: int, alias: str) -> Url:
    url = db.query(Url).filter(Url.user_id == user_id, Url.alias == alias).first()
    return url


def get_all_by_user_id(db: Session, user_id: int) -> list[Url]:
    urls = db.query(Url).filter(Url.user_id == user_id).all()
    return urls


def update(db: Session, user_id: int, alias: str, original: str) -> Url:
    db.query(Url).filter(Url.user_id == user_id, Url.alias == alias).update(
        {"original": original},
        synchronize_session=False,
    )
    db.commit()
    url = get(db, user_id, alias)
    return url


def delete(db: Session, user_id: int, alias: str) -> None:
    db.query(Url).filter(Url.user_id == user_id, Url.alias == alias).delete(
        synchronize_session=False
    )
    db.commit()
