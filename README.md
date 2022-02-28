# John Community Modules

## John 4000 Project
John 4000 is a project of an advanced discord AI chatbot with a range of additional functionalities and features. 

## Community Modules
Due to multiple requests and issues with general use function modules, and a fact that John already contains some modules written by the community, I present to you John Modules Initiative. This repository will contain community modules and shall be used by the community to develop custom John functions they desire.

## John structure and modules
The "community_main" function is run from python file "community_modules.py" from a main john loop. Ideally, every module should be created inside named folder and imported similarly to the GrzechuG example. "community_modules.py" should be used only to execute your imported library. The main john program executes community modules in the following way:

```python
# [...]

# John responds if the following condition is True:
if (
        message.author.name != "John4000"
        and not message.author.name in banlist
        and (
            any([word in message.channel.lower() for word in ['john', 'direct message']])
            or message.channel in ["pogadaj-z-johnem", "john-read-image"]
        )
        
    ): 
        # ADMIN functions are here

        # BASIC modules are here (precoded by th creator)
        
        # COMMUNITY MODULES:
        if await community_modules.community_main(message):
            return

        # AI - builtin AI function is here
        # THE REST...
```

If you don't want john to execute following AI functions, return **True** in community_main function.

Good luck and have fun creating!

_** NOTE ** Previously created modules will be refactored and included here in the following days when necessary consent will be granted._
