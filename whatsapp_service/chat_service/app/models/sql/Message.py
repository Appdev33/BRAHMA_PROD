
from datetime import datetime
from typing import Dict
from interfaces.SqlBaseModel import SqlBaseModel


class Message(SqlBaseModel):
    def __init__(self, sender: str, recipient: str, message_id: str = None, status: str = "sent"):
        self._message_id = message_id
        self._sender = sender
        self._recipient = recipient
        self._status = status
        self._content_type = None  # None until explicitly set

    # Read-only property for message_id
    @property
    def message_id(self) -> str:
        """Get the unique ID of the message."""
        return self._message_id

    # Read-only property for sender
    @property
    def sender(self) -> str:
        """Get the sender of the message."""
        return self._sender

    # Read-only property for recipient
    @property
    def recipient(self) -> str:
        """Get the recipient of the message."""
        return self._recipient

    # Getter and setter for status
    @property
    def status(self) -> str:
        """Get the current status of the message."""
        return self._status

    @status.setter
    def status(self, value: str):
        """Set the message status with validation."""
        allowed_statuses = {"sent", "delivered", "read"}
        if value not in allowed_statuses:
            raise ValueError(f"Invalid status: {value}. Allowed values are: {allowed_statuses}")
        self._status = value

    # Getter and setter for content_type
    @property
    def content_type(self) -> str:
        """Get the content type of the message."""
        return self._content_type or "text/plain"  # Default to 'text/plain' if None

    @content_type.setter
    def content_type(self, value: str):
        """Set the content type with validation."""
        allowed_types = {"text/plain", "text/html", "image/png", "image/jpeg"}
        if value not in allowed_types:
            raise ValueError(f"Invalid content type: {value}. Allowed types are: {allowed_types}")
        self._content_type = value

    def to_dict(self) -> dict:
        """Convert the message to a dictionary representation."""
        return {
            "message_id": self.message_id,
            "sender": self.sender,
            "recipient": self.recipient,
            "status": self.status,
            "content_type": self.content_type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def from_dict(self, data: dict) -> "Message":
        """Load data into the message instance."""
        self._message_id = data.get("message_id", self._message_id)
        self._sender = data["sender"]
        self._recipient = data["recipient"]
        self.status = data.get("status", self.status)
        self.content = data["content"]
        self.content_type = data.get("content_type", self.content_type)
        self.set_timestamps(is_update=True)
        return self
