from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import jwt, JWTError

from app.schemas import TokenPayload
from app import config

JWT_SECRET_KEY = config.jwt.secret
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_MINUTES = 60

pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def create_jwt(data: dict) -> str:
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
    payload.update({"exp": expire})
    token = jwt.encode(payload, JWT_SECRET_KEY)
    return token


def verify_jwt(token: str, credentials_exception) -> TokenPayload:
    try:
        payload = jwt.decode(token, config.jwt.secret, algorithms=[JWT_ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        data: TokenPayload = TokenPayload(sub=user_id)
    except JWTError:
        raise credentials_exception

    return data
