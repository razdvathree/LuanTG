from pyrogram import Client, filters
from plugins.help import module_list
import subprocess
from configurator import prefix


@Client.on_message(filters.command("terminal", prefixes=f'{prefix}') & filters.me)
async def terminal(client,message):
    try:
        cmd = message.text.split(f'{prefix}terminal ')[1]
    except:
        await message.edit('invalid command')
    s = subprocess.getstatusoutput(cmd)
    if s[0] == 0:
        await message.edit(f'command: {cmd}\n{s[1]}')
    else:
        await message.edit(f'Error: {s[1]}')
module_list['terminal'] = f'{prefix}terminal [command]'