import asyncio
import json
from aiohttp import ClientSession, web
from get_weather import get_weather


async def handler(request):
    city = request.rel_url.query['city']

    weather = await get_weather(city)

    result = {'city': city, 'weather': weather}

    return web.Response(text=json.dumps(result, ensure_ascii=False))
