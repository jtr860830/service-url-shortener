from fastapi import APIRouter, status, Path, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.schemas import NewUrlRequest, UrlResponse, UrlsResponse
from app.dependencies import inject_db, inject_user_id_from_token
from app.services import urls as service

router: APIRouter = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UrlResponse)
async def add_url(
    body: NewUrlRequest,
    db: Session = Depends(inject_db),
    user_id: int = Depends(inject_user_id_from_token),
) -> UrlResponse:
    url = service.create(db, user_id, body.original)
    return UrlResponse(data=url)


@router.get(
    "/{id}",
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    response_class=RedirectResponse,
)
async def redirect(
    id: str = Path(description="An alias for specific URL"),
    db: Session = Depends(inject_db),
    user_id: int = Depends(inject_user_id_from_token),
) -> RedirectResponse:
    url = service.get(db, user_id, id)
    return RedirectResponse(url.original)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=UrlsResponse,
)
async def get_all_urls(
    db: Session = Depends(inject_db),
    user_id: int = Depends(inject_user_id_from_token),
) -> UrlsResponse:
    urls = service.get_all_by_user_id(db, user_id)
    return UrlsResponse(data=urls)


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=UrlResponse)
async def update_url(
    body: NewUrlRequest,
    id: str = Path(description="An alias for specific URL"),
    db: Session = Depends(inject_db),
    user_id: int = Depends(inject_user_id_from_token),
) -> UrlResponse:
    url = service.update(db, user_id, id, body.original)
    return UrlResponse(data=url)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_url(
    id: str = Path(description="An alias for specific URL"),
    db: Session = Depends(inject_db),
    user_id: int = Depends(inject_user_id_from_token),
) -> None:
    service.delete(db, user_id, id)
