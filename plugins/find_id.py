from pyrogram import Client, filters
from plugins.help import module_list, file_list
import asyncio
from configurator import prefix

@Client.on_message(filters.command('find_id', prefixes=f'{prefix}') & filters.me)
async def find_id(client, message):
  await message.edit(f'**Айди этого чата:** ```{message.chat.id}```')

module_list['FindIDThisChat'] = f'{prefix}find_id'
