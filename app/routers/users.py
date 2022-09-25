from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.schemas import NewUserRequest, UserResponse
from app.dependencies import inject_db, inject_user_id_from_token
from app.services import users as service

router: APIRouter = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
    body: NewUserRequest, db: Session = Depends(inject_db)
) -> UserResponse:
    data = service.create(db, body.username, body.password)
    msg = "User created successfully"
    return UserResponse(msg=msg, data=data)


@router.get("/me", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user(
    db: Session = Depends(inject_db), user_id: int = Depends(inject_user_id_from_token)
):
    data = service.get(db, user_id)
    msg = "Retrieve user data successfully"
    return UserResponse(msg=msg, data=data)
