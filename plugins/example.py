from pyrogram import Client, filters
from plugins.help import module_list
from configurator import prefix


@Client.on_message(filters.command("example_edit", prefixes=f'{prefix}') & filters.me)
async def example_edit(client, message):
    await message.edit("<code>This is an example module</code>")


module_list['Example'] = f'{prefix}example_edit'
