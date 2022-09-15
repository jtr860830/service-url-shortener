from fastapi import APIRouter, Depends

router: APIRouter = APIRouter(
    prefix="/urls",
    tags=["urls"],
    dependencies=[Depends()],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def add_url():
    pass


@router.get("/{id}")
async def redirect():
    pass


@router.patch("/{id}")
async def update_url():
    pass


@router.delete("/{id}")
async def delete_url():
    pass
