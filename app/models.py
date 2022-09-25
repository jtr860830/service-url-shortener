from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    create_time = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class Url(Base):
    __tablename__ = "urls"
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    alias = Column(String, nullable=False, primary_key=True)
    original = Column(String, nullable=False)
    create_time = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
