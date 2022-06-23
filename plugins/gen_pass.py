from pyrogram import Client, filters
from plugins.help import module_list, file_list
import secrets
import string
import asyncio
from configurator import prefix

@Client.on_message(filters.command('gen_pass', prefixes=f'{prefix}') & filters.me)
async def gen_pass(client, message):
    char = message.text.replace(f'{prefix}gen_pass', '')
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(int(char)))
    await message.edit(f"**Сгенерированный пароль:** ```{password}```")

module_list['GeneratePassword'] = f'{prefix}gen_pass [длина пароля]'
