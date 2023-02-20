import aiohttp
import tokens
from aiogram.types import Message
from dt import time, today

W_TOKEN = tokens.weather_token

async def weather(message: Message):
    city = message.get_args()

    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={W_TOKEN}&units=metric") as resp:
            if resp.status != 200:
                await message.reply("Sorry, I couldn't find the weather for that city. Please try again.")
                return

            weather = await resp.json()

            city = weather["name"]
            country = weather["sys"]["country"]
            temp = weather["main"]["temp"]
            description = weather["weather"][0]["description"]
            wind_speed = weather["wind"]["speed"]

            await message.reply(f"<b>🕐 {time}\n🗓 {today}\n🗺 TZ Europe/Kiyv GMT+2\n\n🌤️ Weather in {city}, {country}: \n🌡️ Temperature: {temp}°C \n☁️ Description: {description.title()} \n💨 Wind Speed: {wind_speed} m/s</b>", parse_mode="HTML") 