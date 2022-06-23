from pyrogram import Client, filters
from plugins.help import module_list
from configurator import version,build,prefix
import platform
from requests import get


# Информация про бота
@Client.on_message(filters.command("info" , prefixes=f"{prefix}") & filters.me)
async def info(client, message):
   platf = ''
   if platform.system == 'Linux' or 'Linux2':
      platf = 'Linux'
   elif platform == 'Darwin':
      platf = 'OS X'
   elif platform == 'Windows':
      platf = 'Windows'
   pic = get(url='https://api.waifu.pics/sfw/waifu').json()
   
   await message.delete()
   await client.send_photo(chat_id=message.chat.id,photo=pic['url'],caption=f'😎DanilaTG UserBot\n🦋Version: {version}\n🧱Build: {build}\n✅Platform: {platf}\n')

module_list['info'] = f'{prefix}info'
