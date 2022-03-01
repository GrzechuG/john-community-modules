from abc import ABC, abstractmethod
from typing import Any, Optional, TypeVar

Message = TypeVar("Message")


class BaseEventHandler(ABC):
    @abstractmethod
    def __call__(self, context: Message) -> Optional[Any]:
        pass
