import logging
import messages
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import Text, Command, ChatTypeFilter
from aiogram.utils.exceptions import InvalidQueryID, MessageTextIsEmpty
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
    elif isinstance(exception, MessageTextIsEmpty):
        await update.message.answer("Please provide a valid message.")
    else:
        await update.message.answer("An error has occurred.")
    return

@dp.message_handler(Text(equals=["/start"], ignore_case=True))
async def cmd_start(message: Message) -> str:

    await message.answer(messages.msg_start,parse_mode="HTML")

@dp.message_handler(Text(equals=["/help"], ignore_case=True))
async def cmd_help(message: Message) -> str:

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

@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE), content_types=['text'])
async def handle_all_messages(message: Message):
    await message.answer("Sorry, I don't understand. Try /help")

dp.register_message_handler(cmd_weather)
dp.register_message_handler(cmd_currency)
dp.register_message_handler(cmd_warmon)
dp.register_message_handler(cmd_iplocate)
dp.register_message_handler(handle_all_messages, ChatTypeFilter(ChatType.PRIVATE))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
