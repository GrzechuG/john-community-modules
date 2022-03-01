import pathlib
import inspect
import glob
import importlib
from typing import List, Type

from .base import BaseEventHandler


def get_handlers(source_package: str = "john_community_modules") -> List[Type[BaseEventHandler]]:
    """
    Tries to discover the handlers in the given package recursively.
    Package name from root is expected.
    """
    search_dir = (pathlib.Path(source_package.replace(".", "/"))).absolute().as_posix()
    module_files = glob.glob(search_dir + "/**/*.py", recursive=True)
    module_files = [x for x in module_files if "__init__" not in x]
    module_files = [pathlib.Path(x).as_posix() for x in module_files]
    module_files = [source_package + "." + x.replace(search_dir + "/", "").replace(".py", "").replace("/", ".") for
                    x in module_files]

    __modules = [inspect.getmembers(importlib.import_module(x)) for x in module_files]
    handlers = []
    for member_modules in __modules:
        for _, member in member_modules:
            if inspect.isclass(member) and issubclass(member, BaseEventHandler) and member != BaseEventHandler:
                handlers.append(member)

    return handlers
