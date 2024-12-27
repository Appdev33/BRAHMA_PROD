# models/interfaces/base_model.py
from abc import ABC, abstractmethod

class BaseModel(ABC):
    """Abstract base model defining the core contract."""

    @property
    @abstractmethod
    def id(self) -> int:
        """Get the unique ID of the model."""
        pass

    @id.setter
    @abstractmethod
    def id(self, value: int):
        """Set the unique ID of the model."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Serialize the model into a dictionary."""
        pass

    @abstractmethod
    def from_dict(self, data: dict) -> "BaseModel":
        """Deserialize data into a model instance."""
        pass
