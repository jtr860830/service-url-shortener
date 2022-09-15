from fastapi import APIRouter, Depends

router: APIRouter = APIRouter(
    prefix="/tokens",
    tags=["tokens"],
    dependencies=[Depends()],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_token():
    pass
