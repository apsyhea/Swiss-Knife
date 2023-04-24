import aiohttp
from aiogram.types import Message
from config import cur_token

C_TOKEN: str = cur_token


async def currency(message: Message) -> None:
    input_parts: list[str] = message.get_args().split()[0:]

    if len(input_parts) != 3:
        await message.reply("Please enter the amount, source currency, and target currency separated by space or try /help")
        return
    amount: float
    source_currency: str
    target_currency: str
    amount, source_currency, target_currency = input_parts

    try:
        amount = float(amount)
    except ValueError:
        await message.reply("Please enter a valid number for the amount.")
        return

    async with aiohttp.ClientSession() as session:
        url: str = f"https://v6.exchangerate-api.com/v6/{C_TOKEN}/latest/{source_currency.upper()}"
        async with session.get(url) as response:
            if response.status != 200:
                await message.reply("Sorry, something went wrong with the currency conversion.")
                return
            data: dict = await response.json()

    rate: float = data["conversion_rates"][target_currency.upper()]
    result: float = amount * rate
    await message.reply(f"<b>💵 {amount} {source_currency.upper()} is {round(result,2)} 💳 {target_currency.upper()}\n\n💻 Dev: @apsyhea</b>", parse_mode="HTML")
