import logging
import requests
import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import
from aiogram.types import Message
from aiogram.utils import executor
from aiogram import types

# API tokens for the bot and OpenWeatherMap API
API_TOKEN = tokens.bot_token
W_TOKEN = tokens.weather_token
C_TOKEN = tokens.cur_token

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

async def currency_convert(message: types.Message):
    if not message.text.startswith('/currency'):
        return

    # split the user input into three parts: amount, source currency, and target currency
    input_parts = message.text.split()[1:]
    if len(input_parts) != 3:
        await message.answer("Please enter the amount, source currency, and target currency separated by spaces.")
        return

    amount, source_currency, target_currency = input_parts

    # check if the amount is a valid number
    try:
        amount = float(amount)
    except ValueError:
        await message.answer("Please enter a valid number for the amount.")
        return

    # make the API request to get the exchange rate
    url = f"https://v6.exchangerate-api.com/v6/{C_TOKEN}/latest/{source_currency.upper()}"
    response = requests.get(url)
    if response.status_code != 200:
        await message.answer("Sorry, something went wrong with the currency conversion.")
        return
    data = response.json()

    # convert the currency and send the result to the user
    rate = data["rates"][target_currency.upper()]
    result = amount * rate
    await message.answer(f"{amount} {source_currency.upper()} = {result} {target_currency.upper()}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
