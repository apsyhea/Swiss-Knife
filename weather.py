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
            stats_str = f'<b>{flag.flag(data["sys"]["country"])}</b>'
            stats_str += f'<b> Country: {data["sys"]["country"]}</b>\n'
            stats_str += f'<b>🌤️ Weather in {data["name"]}, </b>\n'
            stats_str += f'<b>🌡️ Temperature: {data["main"]["temp"]}°C</b>\n'
            stats_str += f'<b>☁️ Description: {data["weather"][0]["description"].title()}</b>\n'
            stats_str += f'<b>💨 Wind Speed: {data["wind"]["speed"]} m/s</b>'

            await message.reply(stats_str, parse_mode="HTML") 