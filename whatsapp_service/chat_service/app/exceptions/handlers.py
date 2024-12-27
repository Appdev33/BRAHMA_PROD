from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from exceptions.base_exceptions import ApplicationError, DatabaseError, EmailAlreadyTakenError, UserNotFoundException
from exceptions.error_dto import ErrorResponseDTO
import logging

logger = logging.getLogger(__name__)

def add_exception_handlers(app: FastAPI):
    @app.exception_handler(ApplicationError)
    async def application_error_handler(request: Request, exc: ApplicationError):
        logger.error(f"ApplicationError: {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content=ErrorResponseDTO(detail=exc.message, status_code=exc.status_code).dict(),
        )

    @app.exception_handler(DatabaseError)
    async def database_error_handler(request: Request, exc: DatabaseError):
        logger.error(f"DatabaseError: {exc.message}")
        return JSONResponse(
            status_code=500,
            content=ErrorResponseDTO(detail=exc.message, status_code=500).dict(),
        )

    @app.exception_handler(EmailAlreadyTakenError)
    async def email_already_taken_error_handler(request: Request, exc: EmailAlreadyTakenError):
        logger.warning(f"EmailAlreadyTakenError: {exc.message}")
        return JSONResponse(
            status_code=400,
            content={
                "detail": exc.message,
                "status_code": 400,
            },
        )

    @app.exception_handler(UserNotFoundException)
    async def user_not_found_handler(request: Request, exc: UserNotFoundException):
        logger.info(f"UserNotFoundException: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content=ErrorResponseDTO(detail=exc.detail, status_code=exc.status_code).dict(),
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled Exception: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content=ErrorResponseDTO(detail="Internal Server Error", status_code=500).dict(),
        )
