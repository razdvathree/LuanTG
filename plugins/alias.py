from pyrogram import Client, filters
from plugins.help import module_list
import asyncio
from configurator import prefix
from fileinput import FileInput
import os
import sys
@Client.on_message(filters.command("alias", prefixes=f'{prefix}') & filters.me)
async def alias(client,message):
    old_prefix = message.text.rsplit('alias')[0]
    new_prefix = message.text.split(f'{prefix}alias ')[1]
    with FileInput('configurator.py',inplace=True) as f:
        for line in f:
            print(line.replace(f"prefix='{old_prefix}'",f"prefix='{new_prefix}'"),end='')
    await message.edit(f'Alias has been updated from {old_prefix} to {new_prefix}\nuse: {new_prefix}alias {old_prefix} for return to back.')
    os.execv(sys.executable,['python']+sys.argv)
module_list['Alias'] = f'{prefix}alias [new prefix]'