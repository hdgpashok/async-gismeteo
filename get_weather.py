import json
from aiohttp import ClientSession, web


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': 'e4f66a04bfaf25cb376d6062a8b1bb94'}

        async with session.get(url= url, params= params) as responce:
            weather_json = await responce.json()
            try:
                return weather_json['weather'][0]['main']
            except KeyError:
                return 'Нет данных'


