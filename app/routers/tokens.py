from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import TokenResponse, LoginRequest, BaseResponse, BaseToken
from app.dependencies import inject_db
from app.models import User
from app.services import tokens, users
from app.utils import verify_password

router: APIRouter = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TokenResponse)
async def create_token(body: LoginRequest, db: Session = Depends(inject_db)):
    user: User = users.get_by_username(db, body.username)

    msg: str = "Create token failed"
    err: str = "Invalid credentials"
    if not user or not verify_password(body.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=BaseResponse(msg=msg, err=err).dict(),
        )

    token: str = tokens.create(user.id)
    data: BaseToken = BaseToken(access_token=token)
    msg = "Create token successfully"
    return TokenResponse(data=data, msg=msg)
