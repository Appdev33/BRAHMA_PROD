from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime

class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, values=None, context=None):  # Add 'context' argument
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return str(v)  # Ensure to return it as a string

class MessageCreate(BaseModel):
    sender_id: ObjectIdStr
    receiver_id: ObjectIdStr
    content: str

class MessageResponse(BaseModel):
    id: ObjectIdStr
    sender_id: ObjectIdStr
    receiver_id: ObjectIdStr
    content: str
    timestamp: datetime

    class Config:
        arbitrary_types_allowed = True




# from pydantic import BaseModel
# from bson import ObjectId
# from datetime import datetime

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
#         return handler.generate_schema(str)


# # Pydantic model for creating a message
# class MessageCreate(BaseModel):
#     sender_id: ObjectIdStr
#     receiver_id: ObjectIdStr
#     content: str

# # Pydantic model for the message response structure
# class MessageResponse(BaseModel):
#     id: ObjectIdStr
#     sender_id: ObjectIdStr
#     receiver_id: ObjectIdStr
#     content: str
#     timestamp: datetime
#     read: bool = False
