import tokens
import requests
from aiogram.types import Message
from dt import time, today

C_TOKEN = tokens.cur_token

async def currency(message: Message):
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
    await message.reply(f"<b>🗓 {today}\n\n💵 {amount} {source_currency.upper()} is {result} 💳 {target_currency.upper()}\n\n💻 Dev: @apsyhea</b>", parse_mode="HTML")