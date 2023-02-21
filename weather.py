import aiohttp
import tokens
import flag
from aiogram.types import Message
from dt import time, today

W_TOKEN = tokens.weather_token

async def weather(message: Message):
    city = message.get_args()

    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={W_TOKEN}&units=metric") as   response:
            if response.status != 200:
                await message.reply("Sorry, I couldn't find the weather for that city. Please try again.")
                return
 
            data = await response.json()
            stats_str = f'{flag.flag(data["sys"]["country"])}'
            stats_str += f' Country: {data["sys"]["country"]}\n'
            stats_str += f'🌤️ Weather in {data["name"]}, \n'
            stats_str += f'🌡️ Temperature: {data["main"]["temp"]}°C\n'
            stats_str += f'☁️ Description: {data["weather"][0]["description"].title()}\n'
            stats_str += f'💨 Wind Speed: {data["wind"]["speed"]} m/s'

            await message.reply(f'<b>{stats_str}</b>', parse_mode="HTML") 