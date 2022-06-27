from pyrogram import Client, filters
from plugins.help import module_list
import asyncio


@Client.on_message(filters.command("spamban", prefixes='!') & filters.me)
async def spamban(client, message):
    await message.edit("Checking your account for Spamban...")
    await client.unblock_user("spambot")
    await client.send_message("spambot", "/start")
    async for iii in client.get_chat_history("spambot", limit=1):
        await message.edit(iii.text)


module_list['SpamBan'] = f'!spamban'
