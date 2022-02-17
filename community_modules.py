import discord
from community_modules.GrzechuG.helloworld import *

async def community_main(message):
	
	# Added by GrzechuG:
	if "test community modules" in message.content:
		await message.channel.send(hello_test(message.content))
		return True
	

