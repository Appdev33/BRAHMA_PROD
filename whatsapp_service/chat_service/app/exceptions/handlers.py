from fastapi import Request, status
from fastapi.responses import JSONResponse
from exceptions.user_exceptions import EmailAlreadyTakenError, UserAlreadyExistsException, UserNotFoundException
from models.error.error_dto import ErrorResponseDTO


async def email_already_taken_exception_handler(request: Request, exc: EmailAlreadyTakenError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ErrorResponseDTO(detail=exc.message, status_code=status.HTTP_400_BAD_REQUEST).dict()
    )


async def user_already_exists_exception_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ErrorResponseDTO(detail=exc.message, status_code=status.HTTP_400_BAD_REQUEST).dict()
    )


async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=ErrorResponseDTO(detail=exc.message, status_code=status.HTTP_404_NOT_FOUND).dict()
    )
