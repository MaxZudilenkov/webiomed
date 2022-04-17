import random
import json
import time
from aiohttp import web, ClientSession, request


async def get_photos(request):
    # Метод для вывода фотографий в шаблон
    f = open('json_photos.json')
    file_content = f.read()
    return web.Response(text=str(file_content))

async def get_posts(request):
    # Метод для вывода постов в шаблон
    f = open('json_posts.json')
    file_content = f.read()
    return web.Response(text=str(file_content))

async def get_posts_and_photos(request):
    # Метод для вывода в шаблон объединенных данных
    f1data = f2data = ""
    with open('json_posts.json') as f1:
        f1data = f1.read()
    with open('json_photos.json') as f2:
        f2data = f2.read()
    f1data += ", "
    f1data += f2data
    f3 = '(' + f1data + ')'

    return web.Response(text=str(f3))


app = web.Application()
app.add_routes([web.get('/api/photos', get_photos)])
app.add_routes([web.get('/api/posts', get_posts)])
app.add_routes([web.get('/api/posts_and_photos', get_posts_and_photos)])
web.run_app(app)
