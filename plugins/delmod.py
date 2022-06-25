from pyrogram import Client,filters
from plugins.help import module_list
from configurator import prefix
import os
import sys

@Client.on_message(filters.command("delmod", prefixes=prefix) & filters.me)
async def delete_module(client,message):
  try:
    mod_for_delete = message.text.split(f'{prefix}delmod ')[1]
  except:
    await message.edit('This module is not available')
  try:
    os.remove(f'plugins/{mod_for_delete}')
    await message.edit('The module has been successfully removed!')
    os.execv(sys.executable,['python']+sys.argv)
  except Exception as e:
    await message.edit('Oops error: ',e)
    
module_list['DeleteModule'] = f'{prefix}delmod [module name.py]'
