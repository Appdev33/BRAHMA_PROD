# models/interfaces/sql_base_model.py
from datetime import datetime
from interfaces.BaseModel import BaseModel
from abc import abstractmethod

class SQLBaseModel(BaseModel):
    """SQL Base interface defining common timestamp fields."""

    @property
    @abstractmethod
    def created_at(self) -> datetime:
        """Get the creation timestamp."""
        pass

    @property
    @abstractmethod
    def updated_at(self) -> datetime:
        """Get the last updated timestamp."""
        pass

    @abstractmethod
    def set_timestamps(self, is_update: bool = False):
        """Set timestamps for creation or update."""
        pass
