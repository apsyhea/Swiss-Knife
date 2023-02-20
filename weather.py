import aiohttp
import tokens
from aiogram.types import Message

W_TOKEN = tokens.weather_token

async def weather(message: Message, city: str):
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

            await message.reply(f"Weather in {city}, {country}: \n\nTemperature: {temp}°C \nDescription: {description} \nWind Speed: {wind_speed} m/s")
