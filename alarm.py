# import datetime
import asyncio
import aiohttp
from tokens import alarm_token
from aiogram.types import Message


A_TOKEN = alarm_token


async def make_request():
    url = 'https://alerts.com.ua/api/states'
    headers = {'X-API-Key': f'{A_TOKEN}'}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response_text = await response.text()
            print(response_text)

asyncio.run(make_request())
