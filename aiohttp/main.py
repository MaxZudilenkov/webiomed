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
    posts = open('json_posts.json')
    photos = open('json_photos.json')
    file_content = posts.read(), photos.read()
    return web.Response(text=str(file_content))


app = web.Application()
app.add_routes([web.get('/photos', get_photos)])
app.add_routes([web.get('/posts', get_posts)])
app.add_routes([web.get('/posts_and_photos', get_posts_and_photos)])
web.run_app(app)
