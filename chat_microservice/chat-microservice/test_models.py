from datetime import datetime
from bson import ObjectId
from app.schemas.message_schema import MessageCreate, MessageResponse
from app.models.message import TextMessage, ObjectIdStr

def run_tests():
    # Test MessageCreate
    try:
        message_data = {
            "sender_id": ObjectIdStr("507f1f77bcf86cd799439011"),
            "receiver_id": ObjectIdStr("507f1f77bcf86cd799439012"),
            "content": "Hello, World!"
        }
        message_create = MessageCreate(**message_data)
        print("MessageCreate Test Passed")
    except Exception as e:
        print(f"MessageCreate Test Failed: {e}")

    # Test MessageResponse
    try:
        response_data = {
            "id": ObjectIdStr("507f1f77bcf86cd799439013"),
            "sender_id": ObjectIdStr("507f1f77bcf86cd799439011"),
            "receiver_id": ObjectIdStr("507f1f77bcf86cd799439012"),
            "content": "Hello, World!",
            "timestamp": datetime.now(),
            "read": False
        }
        message_response = MessageResponse(**response_data)
        print("MessageResponse Test Passed")
    except Exception as e:
        print(f"MessageResponse Test Failed: {e}")

    # Test TextMessage
    try:
        text_message = TextMessage(
            id=ObjectIdStr("507f1f77bcf86cd799439013"),
            sender_id=ObjectIdStr("507f1f77bcf86cd799439011"),
            receiver_id=ObjectIdStr("507f1f77bcf86cd799439012"),
            content="Hello, World!",
            timestamp=datetime.now(),
            read=False
        )
        assert text_message.get_type() == "text"
        serialized_message = text_message.serialize()
        print("TextMessage Test Passed")
    except Exception as e:
        print(f"TextMessage Test Failed: {e}")

if __name__ == "__main__":
    run_tests()
