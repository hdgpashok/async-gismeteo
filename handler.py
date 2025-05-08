import asyncio
import json
from aiohttp import ClientSession, web
from get_translation import get_translation
from get_weather import get_weather


async def handler(request):
    city_ru = request.rel_url.query['city']
    city_eng = await get_translation(city_ru, 'ru', 'end')

    weather_eng = await get_weather(city_eng)
    weather_ru = await get_translation(weather_eng, 'end', 'ru')

    result = {'city' : city_ru, 'weather' : weather_ru}

    return web.Response(text=json.dumps(result, ensure_ascii= False))