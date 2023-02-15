import tokens
import logging
import aiohttp
import requests
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from aiogram.dispatcher.filters import Text, Command

API_TOKEN = tokens.bot_token
W_TOKEN = tokens.weather_token
C_TOKEN = tokens.cur_token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(Text(equals=["/start"], ignore_case=True))
async def cmd_start(message: Message):
    dp.register_message_handler(process_city, commands=['weather'])
    dp.register_message_handler(currency_convert, commands=['currency'])
    await message.answer("""
Hello, I'm a Swiss Knife bot. 
\nTo display the current weather 
type: /weather [city] 
For example /weather Tokyo:
\nTo convert the exchange rate 
type: /currency [number][currency][currency]
For example: /currency 1 eur usd""")

@dp.message_handler(Command("weather"))
#async def currency_convert(message: types.Message):
async def process_city(message: Message):
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

            await message.reply(f"Weather in {city}, {country}: \n\nTemperature: {temp}°C \nDescription: {description} \nWind Speed: {wind_speed} m/s")

@dp.message_handler(Command("currency"))
async def currency_convert(message: types.Message):
    input_parts = message.get_args().split()[0:]
    if len(input_parts) != 3:
        await message.reply("Please enter the amount, source currency, and target currency separated by spaces.")
        return

    amount, source_currency, target_currency = input_parts

    try:
        amount = float(amount)
    except ValueError:
        await message.reply("Please enter a valid number for the amount.")
        return

    url = f"https://v6.exchangerate-api.com/v6/{C_TOKEN}/latest/{source_currency.upper()}"

    response = requests.get(url)
    if response.status_code != 200:
        await message.reply("Sorry, something went wrong with the currency conversion.")
        return
    data = response.json()

    rate = data["conversion_rates"][target_currency.upper()]
    result = amount * rate
    await message.reply(f"{amount} {source_currency.upper()} = {result} {target_currency.upper()}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)