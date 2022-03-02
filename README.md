# John Community Modules

## John 4000 Project
John 4000 is a project of an advanced discord AI chatbot with a range of additional functionalities and features. 

## Community Modules
Due to multiple requests and issues with general use function modules, and a fact that John already contains some modules written by the community, I present to you John Modules Initiative. This repository will contain community modules and shall be used by the community to develop custom John functions they desire.

## John structure and modules
To create a new module, create a folder in john-community-modules with the name of your new module. 

In this folder, you should create two files:

* __init__.py
* handler.py

In handler.py you should create your main class as follows (where ModuleName is your module name):
```python
class ModuleName(BaseEventHandler):
    def __init__(self):
        super().__init__()
       # YOUR CODE #

    async def __call__(self, context: Message) -> Optional[Any]: 
        if "part of message" in context.content: # Check whether message send to john contains "part of message"
                 # YOUR CODE #
                 await context.channel.send(result) # Send message to the same channel the message came from.
            return True # Retrun True if you don't want AI function in john to be executed after your module
        
        return False # Retrun False at the end of the funcion (in case your module was not activated)
```

Variable `context` passed is message object from discord API (https://discordpy.readthedocs.io/en/stable/api.html#message)

If you don't want john to execute AI functions that follow community modules, return **True** from `__call__` function. If your module was not activated, return **False**.

`__init__.py` content should be as following:
```python
from .handler import ModuleName
```
If you have further problems, take a look at an example module `Troll Moule`.

Good luck and have fun creating!

_** NOTE ** Previously created modules will be refactored and included here in the following days when necessary consent will be granted._

## How to contribute?

- fork this repo
- make your changes at your own new branch in forked repo
- make pull request
