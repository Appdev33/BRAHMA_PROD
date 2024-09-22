from pydantic import BaseModel, EmailStr
from bson import ObjectId

class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, values=None, context=None):  # Add 'context' argument
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return str(v)  # Ensure to return it as a string

class UserCreate(BaseModel):
    username: str
    email: EmailStr

class UserResponse(BaseModel):
    id: ObjectIdStr
    username: str
    email: EmailStr

    class Config:
        arbitrary_types_allowed = True






# from pydantic import BaseModel, EmailStr
# from bson import ObjectId

# class ObjectIdStr(str):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError('Invalid ObjectId')
#         return ObjectId(v)

#     @classmethod
#     def __get_pydantic_core_schema__(cls, source: type, handler) -> None:
#         return handler.generate_schema(str)  # Use `str` as the underlying type

# class UserCreate(BaseModel):
#     username: str
#     email: EmailStr

# class UserResponse(BaseModel):
#     id: ObjectIdStr
#     username: str
#     email: EmailStr

#     class Config:
#         arbitrary_types_allowed = True
