from abc import ABC, abstractmethod
import datetime

class NoSqlModel(ABC):

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

