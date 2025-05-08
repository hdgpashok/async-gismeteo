import json
from aiohttp import ClientSession, web


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url= url, params= params) as responce:
            weather_json = await responce.json()
            try:
                return weather_json['weather'][0]['main']
            except KeyError:
                return 'Нет данных'


