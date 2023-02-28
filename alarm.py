# import datetime
import json
import aiohttp
from tokens import alarm_token
from aiogram.types import Message


A_TOKEN = alarm_token


async def alarm(message: Message):
    url = 'https://alerts.com.ua/api/states'
    headers = {'X-API-Key': f'{A_TOKEN}'}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                await message.reply("Sorry, something went wrong. Server API temporarily May not be available.")
                return
            data = await response.text()
            state = json.loads(data)
            for alarm_state in state['states']:
                if alarm_state['alert']:
                    await message.reply(f"{alarm_state['name']} повітряна тривога")