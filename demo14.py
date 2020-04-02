from aiohttp import web
import asyncio

async def home(request: web.Request) -> web.Response:
    await asyncio.sleep(3)
    return web.Response(text="Hi")


async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes([web.get("/", home)])
    return app


web.run_app(init_app(), port=5000)
