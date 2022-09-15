from fastapi import APIRouter, Depends

router: APIRouter = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends()],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_user():
    pass


@router.get("/me")
async def get_user():
    pass
