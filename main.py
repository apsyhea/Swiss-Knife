import tokens
import messages
import logging
from warmon import warmon
from weather import weather
from currency import currency
from geoip import ip
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor
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
    dp.register_message_handler(weather, commands=['weather'])
    dp.register_message_handler(currency, commands=['currency'])
    dp.register_message_handler(warmon, commands=['warmon'])
    dp.register_message_handler(ip, commands=['ip'])
    await message.answer(messages.msg_start,parse_mode="HTML")

@dp.message_handler(Command("weather"))
async def cmd_weather(message: Message):
    await weather(message)

@dp.message_handler(Command("currency"))
async def cmd_currency(message: Message):
    await currency(message)

@dp.message_handler(Command("warmon"))
async def cmd_warmon(message: Message):
    await warmon(message)


@dp.message_handler(Command("ip"))
async def cmd_ip(message: Message):
    await ip(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)