import logging
import messages
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.dispatcher.filters import Text, Command
from aiogram.utils.exceptions import InvalidQueryID
from tokens import bot_token, weather_token, cur_token
from warmon import warmon
from weather import weather
from currency import currency
from iplocate import iplocate

API_TOKEN = bot_token
W_TOKEN = weather_token
C_TOKEN = cur_token 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.errors_handler()
async def errors_handler(update, exception) -> str:
    if isinstance(exception, InvalidQueryID):
        await update.message.answer("Command not recognized. Please try again.")
        return
    raise exception

@dp.message_handler(Text(equals=["/start"], ignore_case=True))
async def cmd_start(message: Message) -> str:
    dp.register_message_handler(weather, commands=['weather'])
    dp.register_message_handler(currency, commands=['currency'])
    dp.register_message_handler(warmon, commands=['warmon'])
    dp.register_message_handler(iplocate, commands=['iplocate'])
    await message.answer(messages.msg_start,parse_mode="HTML")

@dp.message_handler(Command("weather"))
async def cmd_weather(message: Message) -> str:
    await weather(message)

@dp.message_handler(Command("currency"))
async def cmd_currency(message: Message) -> str:
    await currency(message)

@dp.message_handler(Command("warmon"))
async def cmd_warmon(message: Message) -> str:
    await warmon(message)


@dp.message_handler(Command("iplocate"))
async def cmd_iplocate(message: Message) -> str:
    await iplocate(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)