import discord

from john_community_modules.example_module import *


async def community_main(message):

    # Added by GrzechuG:
    if "test community modules" in message.content:
        await message.channel.send(hello())
        return True
