from abc import ABC, abstractmethod
from typing import List, Generic, TypeVar

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def create(self, item: T) -> T:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get_by_id(self, item_id: str) -> T:
        pass


# from abc import ABC, abstractmethod
# from typing import List, Generic, TypeVar

# T = TypeVar('T')

# class BaseRepository(ABC, Generic[T]):
#     @abstractmethod
#     def create(self, item: T) -> T:
#         pass

#     @abstractmethod
#     def get_all(self) -> List[T]:
#         pass

#     @abstractmethod
#     def get_by_id(self, item_id: str) -> T:
#         pass

