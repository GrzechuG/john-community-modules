from typing import Any, Optional

from john_community_modules.base import BaseEventHandler, Message


class TrollHandler(BaseEventHandler):
    def __init__(self, troll_message: str = "💩"):
        super().__init__()
        self.troll_message = troll_message

    def __call__(self, context: Message) -> Optional[Any]:
        return self.troll_message
