import tokens
import subprocess
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Set up the bot and dispatcher
TOKEN = tokens.test_token
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Define the command for the bot
@dp.message_handler(commands=['ping'])
async def ping(message: types.Message):
    # Get the IP address from the command argument
    ip_address = message.get_args()
    print(ip_address)
    # Ping the IP address and get the result
    result = subprocess.run(['ping', ip_address], capture_output=True)

    # Send the result to the user
    if result.returncode == 0:
        response = f'Ping result for {ip_address}:\n\n{result.stdout.decode()}'
    else:
        response = f'Ping failed for {ip_address}:\n\n{result.stderr.decode()}'

    await bot.send_message(message.chat.id, response, parse_mode=ParseMode.HTML)

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)