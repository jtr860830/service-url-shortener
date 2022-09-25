from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas import BaseResponse
from app.routers import users, tokens, urls

app: FastAPI = FastAPI(title="URL Shortener APIs")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def initialize():
    pass


@app.on_event("shutdown")
async def cleanup():
    pass


@app.exception_handler(HTTPException)
async def http_error_handler(_, exc: HTTPException) -> JSONResponse:
    return JSONResponse(exc.detail, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_error_handler(_, exc: RequestValidationError) -> JSONResponse:
    msg: str = "Validation error"
    err: list = exc.errors()
    return JSONResponse(
        BaseResponse(msg=msg, err=err).dict(),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(tokens.router, prefix="/tokens", tags=["tokens"])
app.include_router(urls.router, prefix="/urls", tags=["urls"])
