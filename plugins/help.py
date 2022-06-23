from pyrogram import Client, filters
import asyncio
from configurator import prefix

module_list = {}
requirements_list = []
file_list = {}

@Client.on_message(filters.command('help', prefixes=f'{prefix}') & filters.me)
async def help(client, message):
    list = []
    for k, v in module_list.items():
        list.append(f'**• {k}**: ```{v}```')
    a = " "
    for i in list:
        a = a.lstrip() + f'{i}\n'
    await message.edit(f"""
**{len(module_list)} available modules.**
{a}""")

module_list['Help'] = f'{prefix}help'
