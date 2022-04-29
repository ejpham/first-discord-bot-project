import discord
from discord.utils import get
from typing import List

intents = discord.Intents.default()
intents.messages = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'bing' in message.content:
        await message.reply('bong')
    
    if any(s in message.content for s in ['ok', 'Ok', 'OK']):
        await message.add_reaction('<:yuiOk:914639438880063550>')
    
    if message.content.startswith('o phi o phi'):
        await message.reply('g!')

@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(969541681655468042)
    if message.channel.id == 969541681655468042:
        return
    embeds = []
    deleted_message = discord.Embed(title='A message has been deleted.')
    deleted_message.set_author(name=f'{message.author.display_name}', icon_url=f'{message.author.avatar_url}')
    deleted_message.add_field(name='Content', value=f'{message.content}')
    embeds.append(deleted_message)
    imgcount = othercount = 0
    for i, value in enumerate(message.attachments):
        if message.attachments[i].url.endswith(('jpg', 'jpeg', 'png', 'gif', 'heic', 'raw', 'tif', 'tiff', 'bmp')):
            imgcount += 1
            image = discord.Embed(title='Image ' + str(imgcount))
            image.set_author(name=f'{message.author.display_name}', icon_url=f'{message.author.avatar_url}')
            image.set_image(url=f'{message.attachments[i].url}')
            embeds.append(image)
        else:
            othercount += 1
            deleted_message.add_field(name='Attachment ' + str(othercount), value=f'{message.attachments[i].url}')
    for i, value in enumerate(embeds):
        await channel.send(embed=embeds[i])

bot.run('')
