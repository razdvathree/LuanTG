import os
import wget
from pyrogram import Client, filters
from plugins.help import module_list
from configurator import prefix
import sys
@Client.on_message(filters.command('loadmod', prefixes=f'{prefix}') & filters.me)
async def loadmod(client, message):
    if not message.reply_to_message:
        await message.edit("<b>Load module...</b>")
        link = message.command[1]
        wget.download(link, 'plugins/')
        await message.edit(
            f"<b>The module has been loaded successfully."
        )
    else:
        await client.download_media(message.reply_to_message.document, file_name='plugins/')
        await message.edit(
            f"<b>The module has been loaded successfully."
        )
    os.execv(sys.executable,['python']+sys.argv)
    
module_list['Loadmod'] = f'{prefix}loadmod [ссылка на модуль]'
