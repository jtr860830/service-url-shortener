from fastapi import Depends, status, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.database import SessionLocal
from app.schemas import BaseResponse, TokenPayload
from app.utils import verify_jwt

bearer_token = HTTPBearer()


def inject_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def inject_user_id_from_token(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_token),
) -> TokenPayload:
    token: str = credentials.credentials
    msg: str = "Verify token failed"
    err: str = "Invalid credentials"
    exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=BaseResponse(msg=msg, err=err).dict(),
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_payload: TokenPayload = verify_jwt(token, exception)
    return token_payload.sub
