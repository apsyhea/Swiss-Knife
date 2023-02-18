import tokens
import logging
import aiohttp
import requests
from datetime import date
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text, Command

API_TOKEN = tokens.bot_token
W_TOKEN = tokens.weather_token
C_TOKEN = tokens.cur_token

logging.basicConfig(level=logging.INFO)

today = date.today()

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(Text(equals=["/start"], ignore_case=True))
async def cmd_start(message: Message):
    dp.register_message_handler(process_city, commands=['weather'])
    dp.register_message_handler(currency_convert, commands=['currency'])
    dp.register_message_handler(warmon, commands=['warmon'])
    await message.answer("""
Hello, I'm a Swiss Knife bot. 
\nTo display the current weather 
type: /weather [city] 
For example /weather Tokyo:
\nTo convert the exchange rate 
type: /currency [number][currency][currency]
For example: /currency 1 eur usd
\nUse /warmon to display rashist casualty statistics for the day
""")

@dp.message_handler(Command("weather"))
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

            await message.reply(f"📅 <b>As of {today}</b>\n\n🌤️ Weather in {city}, {country}: \n🌡️ Temperature: {temp}°C \n☁️ Description: {description} \n💨 Wind Speed: {wind_speed} m/s", parse_mode="HTML") 

@dp.message_handler(Command("currency"))
async def currency_convert(message: Message):
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
    await message.reply(f"📅 <b>As of {today}</b>\n\n💵 {amount} {source_currency.upper()} is {result} 💳 {target_currency.upper()}", parse_mode="HTML")

@dp.message_handler(Command('warmon'))
async def warmon(message: Message):
    
    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    response = requests.get(url)
    if response.status_code != 200:
        await message.reply("Sorry, something went wrong. Server API temporarily May not be available.")
        return

    data = response.json()

    stats = data['data']['stats']
    stats_str = f"Personnel Units: {stats['personnel_units']}\n"
    stats_str += f"Tanks: {stats['tanks']}\n"
    stats_str += f"Armoured Fighting Vehicles: {stats['armoured_fighting_vehicles']}\n"
    stats_str += f"Artillery Systems: {stats['artillery_systems']}\n"
    stats_str += f"MLRS: {stats['mlrs']}\n"
    stats_str += f"AA Warfare Systems: {stats['aa_warfare_systems']}\n"
    stats_str += f"Planes: {stats['planes']}\n"
    stats_str += f"Helicopters: {stats['helicopters']}\n"
    stats_str += f"Vehicles Fuel Tanks: {stats['vehicles_fuel_tanks']}\n"
    stats_str += f"Warships Cutters: {stats['warships_cutters']}\n"
    stats_str += f"Cruise Missiles: {stats['cruise_missiles']}\n"
    stats_str += f"UAV Systems: {stats['uav_systems']}\n"
    stats_str += f"Special Military Equip: {stats['special_military_equip']}\n"
    stats_str += f"ATGM/SRBM Systems: {stats['atgm_srbm_systems']}\n"

    await message.reply(f'📅 <b>As of {today}\n\n🐷 loss of pigs:</b>\n<code>{stats_str}</code>', parse_mode="HTML")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
