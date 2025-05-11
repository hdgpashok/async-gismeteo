import asyncio

from handler import handler
from aiohttp import web


async def main():
    app = web.Application()
    app.add_routes([web.get('/weather', handler)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    while True:
        await asyncio.sleep(3600)


if __name__ == '__main__':
    asyncio.run(main())