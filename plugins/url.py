from pyrogram import Client, filters
from plugins.help import module_list
from requests import post
from configurator import prefix

@Client.on_message(filters.command("gg", prefixes=f'{prefix}') & filters.me)
async def gg(client,message):
    try:
        site = message.text.split(f'{prefix}gg ')[1]
    except:
        await message.edit('Invalid url')
    if 'http://' not in site and 'https://' not in site:
        site = f'http://{site}'
    await message.edit(f'Url: {site} check...')
    check = post(
        'http://gg.gg/check',
        data={
            'custom_path': None,
            'use_norefs': '0',
            'long_url': site,
            'app': 'site',
            'version': '0.1'
        }
    ).text
    if check == 'ok':
        short = post(
            'http://gg.gg/create',
            data={
                'custom_path': None,
                'use_norefs': '0',
                'long_url': site,
                'app': 'site',
                'version': '0.1'
            }
        ).text
        await message.edit(short)

module_list['url'] = f'{prefix}gg [link on site]'