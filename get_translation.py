import json
from aiohttp import ClientSession, web


async def get_translation(text, source, target):
    async with ClientSession() as session:
        url = 'https://libretranslate.de/translate'
        data = {'q': text, 'source': source, 'target': target, 'format': 'text'}

        async with session.post(url= url, json= data) as responce:
            translate_json = await responce.json()

            try:
                return translate_json['translatedText']
            except KeyError:
                return text

