import logging
import messages
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import Text, Command, ChatTypeFilter
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


@dp.message_handler(Text(equals=["/start"], ignore_case=True))
async def cmd_start(message: Message):

    await message.answer(messages.msg_start, parse_mode="HTML")


@dp.message_handler(Command("help"))
async def cmd_help(message: Message):

    await message.reply(messages.msg_start, parse_mode="HTML")


@dp.message_handler(Command("weather"))
async def cmd_weather(message: Message):

    await weather(message)


@dp.message_handler(Command("currency"))
async def cmd_currency(message: Message):

    await currency(message)


@dp.message_handler(Command("warmon"))
async def cmd_warmon(message: Message):

    await warmon(message)


@dp.message_handler(Command("iplocate"))
async def cmd_iplocate(message: Message):

    await iplocate(message)


@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE), content_types=['text'])
async def handle_all_messages(message: Message):

    await message.answer("Sorry, I don't understand. Try /help")

dp.register_message_handler(cmd_help, commands=['help'])
dp.register_message_handler(weather, commands=['weather'])
dp.register_message_handler(currency, commands=['currency'])
dp.register_message_handler(warmon, commands=['warmon'])
dp.register_message_handler(iplocate, commands=['iplocate'])
dp.register_message_handler(
    handle_all_messages, ChatTypeFilter(ChatType.PRIVATE))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
