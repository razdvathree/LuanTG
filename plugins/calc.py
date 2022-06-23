from pyrogram import Client, filters
from plugins.help import module_list
from configurator import prefix

@Client.on_message(filters.command("calc", prefixes=f'{prefix}') & filters.me)
async def calculator(client, message):
    try:
        question = message.text.split(f'{prefix}calc ')[1]
    except:
        await message.edit('2+2=5')
    try:
        answer = eval(question)
        answer = f"<b>{question}=</b><code>{answer}</code>"
    except Exception as e:
        answer = f"<b>{question}=</b><code>{e}</code>"
    await message.edit(answer)




module_list['Example'] = f'{prefix}calc [1+1]'