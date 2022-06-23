from pyrogram import Client, filters
from plugins.help import module_list
from configurator import prefix
import os
import sys

@Client.on_message(filters.command('restart', prefixes=f'{prefix}') & filters.me)
async def restart(client,message):
    await message.edit('restarting...')
    await message.edit('restart is successfully!')
    os.execv(sys.executable,['python']+sys.argv)
module_list['Restart'] = f"{prefix}restart"
    