import tokens
import logging
import requests
import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message

API_TOKEN = tokens.bot_token
W_TOKEN = tokens.weather_token
C_TOKEN = tokens.cur_token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'], state=None)
@dp.message_handler(commands=['help'], state=None)
async def cmd_start(message: Message):

    await message.answer("Hello i am Swiss Knife bot")

@dp.message_handler(lambda message: message.text.lower() != 'cancel', state=None)
async def process_city(message: Message):
    if not message.text.startswith('/weather'):
        return

    city = message.text[len('/weather'):].strip()

    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={W_TOKEN}&units=metric") as resp:
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

@dp.message_handler(lambda message: message.text.lower() != 'cancel', state=None)
async def currency_convert(message: types.Message):
    if not message.text.startswith('/currency'):
        return

    input_parts = message.text.split()[1:]
    if len(input_parts) != 3:
        await bot.send_message(chat_id=message.chat.id, text="Please enter the amount, source currency, and target currency separated by spaces.")
        return

    amount, source_currency, target_currency = input_parts

    try:
        amount = float(amount)
    except ValueError:
        await bot.send_message(chat_id=message.chat.id, text="Please enter a valid number for the amount.")
        return

    url = f"https://v6.exchangerate-api.com/v6/{C_TOKEN}/latest/{source_currency.upper()}"

    response = requests.get(url)
    if response.status_code != 200:
        await bot.send_message(chat_id=message.chat.id, text="Sorry, something went wrong with the currency conversion.")
        return
    data = response.json()

    rate = data["conversion_rates"][target_currency.upper()]
    result = amount * rate
    await bot.send_message(chat_id=message.chat.id, text=f"{amount} {source_currency.upper()} = {result} {target_currency.upper()}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)