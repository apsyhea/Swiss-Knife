import logging
import aiohttp
import tokens
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode, Message
from aiogram.utils import executor

# API tokens for the bot and OpenWeatherMap API
API_TOKEN = tokens.bot_token
APPID = tokens.weather_token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Handle /start and /help command
@dp.message_handler(commands='start', state='*')
@dp.message_handler(commands='help', state='*')
async def cmd_start(message: Message):
    """
    Handle /start and /help command
    """
    await message.answer("Hi there! I am a weather bot. Send me the name of a city and I will display the current weather conditions.")

# Handle messages that contain city names
@dp.message_handler(lambda message: message.text not in ['cancel'], state='*')
@dp.message_handler(lambda message: message.text.lower() not in ['cancel'], state='*')
async def process_city(message: Message):
    if not message.text.startswith('/weather'):
        return

    city = message.text[len('/weather'):].strip()

    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APPID}&units=metric") as resp:
            if resp.status != 200:
                await bot.send_message(chat_id=message.chat.id, text="Sorry, I couldn't find the weather for that city. Please try again.")
                return

            weather = await resp.json()

            city = weather["name"]
            country = weather["sys"]["country"]
            temp = weather["main"]["temp"]
            description = weather["weather"][0]["description"]
            wind_speed = weather["wind"]["speed"]

            await bot.send_message(chat_id=message.chat.id, text=f"Weather in {city}, {country}: \n\nTemperature: {temp}°C \nDescription: {description} \nWind Speed: {wind_speed} m/s")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
