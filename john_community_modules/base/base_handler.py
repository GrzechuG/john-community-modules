from abc import ABC, abstractmethod
from typing import Any, List, Optional, Type, TypeVar

Message = TypeVar("Message")


class BaseEventHandler(ABC):
    @abstractmethod
    def __call__(self, context: Message) -> Optional[Any]:
        pass


def get_all_handlers() -> List[Type[BaseEventHandler]]:
    return [_subclass for _subclass in BaseEventHandler.__subclasses__()]