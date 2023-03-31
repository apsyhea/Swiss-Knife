"""Import necessary libraries and modules."""
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import ChatTypeFilter, Command, Text
from aiogram.types import ChatType, Message
# Importing API tokens and keys from a separate module
from config import bot_token
# Importing user-defined modules
import modules.messages as messages
from modules.warmon import warmon
from modules.weather import weather
from modules.currency import currency
from modules.iplocate import iplocate
from modules.alarm import alarm

API_TOKEN: str = bot_token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(Text(equals=["/start"], ignore_case=True))
# Handler for "/start" command
async def cmd_start(message: Message) -> None:
    """
    Sends a welcome message when the user sends "/start" command
    """
    await message.answer(messages.msg_start, parse_mode="HTML")


@dp.message_handler(Command("help"))
# Handler for "/help" command
async def cmd_help(message: Message) -> None:
    """
    Sends a help message when the user sends "/help" command
    """
    await message.reply(messages.msg_start, parse_mode="HTML")


@dp.message_handler(Command("changelog"))
# Handler for "/help" command
async def cmd_changelog(message: Message) -> None:
    """
    Sends a help message when the user sends "/help" command
    """
    await message.reply(messages.msg_changelog, disable_web_page_preview=True, parse_mode="HTML")


@dp.message_handler(Command("weather"))
# Handler for "/weather" command
async def cmd_weather(message: Message) -> None:
    """
    Calls the weather function to provide weather information
    """
    await weather(message)


@dp.message_handler(Command("currency"))
# Handler for "/currency" command
async def cmd_currency(message: Message) -> None:
    """
    Calls the currency function to provide currency conversion information
    """
    await currency(message)


@dp.message_handler(Command("warmon"))
# Handler for "/warmon" command
async def cmd_warmon(message: Message) -> None:
    """
    Calls the warmon function to provide weather monitoring information
    """
    await warmon(message)


@dp.message_handler(Command("iplocate"))
# Handler for "/iplocate" command
async def cmd_iplocate(message: Message) -> None:
    """
    Calls the iplocate function to provide IP location information
    """
    await iplocate(message)


@dp.message_handler(Command("alarm"))
# Handler for "/alarm" command
async def cmd_alarm(message: Message) -> None:
    """
    Calls the alarm function...
    """
    await alarm(message)


@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE), content_types=['text'])
# Handler for all other messages in private chat
async def handle_all_messages(message: Message) -> None:
    """
    Responds with a default message for other messages in private chat
    """
    await message.answer("Sorry, I don't understand. Try /help")

dp.register_message_handler(cmd_help, commands=['help'])
dp.register_message_handler(cmd_changelog, commands=['changelog'])
dp.register_message_handler(weather, commands=['weather'])
dp.register_message_handler(currency, commands=['currency'])
dp.register_message_handler(warmon, commands=['warmon'])
dp.register_message_handler(iplocate, commands=['iplocate'])
dp.register_message_handler(alarm, commands=['alarm'])
dp.register_message_handler(
    handle_all_messages, ChatTypeFilter(ChatType.PRIVATE))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

