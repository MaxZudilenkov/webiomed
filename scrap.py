import asyncio
import json
import random
import time
from aiohttp import ClientSession


async def create_json(url, file):
    # Метод для сбора данных с указанных адресов
    url = url
    async with ClientSession() as session:
        async with session.get(url) as response:
            random_number = random.randint(0, 10)
            json_data = await response.json()
            for key in json_data:
                key['title'] = key['title'] + str(random_number)
            with open(f'{file}', 'w') as outfile:
                json.dump(json_data, outfile)


def server_time():
    read_file = open("server_time", "r")
    request_time = int(read_file.read())
    return request_time


async def routine():
    while True:
        time.sleep(server_time())
        await create_json('http://jsonplaceholder.typicode.com/photos', 'json_photos.json')
        await create_json('http://jsonplaceholder.typicode.com/posts', 'json_posts.json')


asyncio.run(routine())
