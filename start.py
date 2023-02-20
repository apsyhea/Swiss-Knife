from aiogram.types import Message

async def start(message: Message):
    dp.register_message_handler(weather, commands=['weather'])
    dp.register_message_handler(currency, commands=['currency'])
    dp.register_message_handler(warmon, commands=['warmon'])
    await message.answer("""
<b>Hello, I'm a Swiss Knife bot. 
\nTo display the current weather 
type: /weather [city] 
For example <code>/weather Tokyo</code>
\nTo convert the exchange rate 
type: /currency [number][currency][currency]
For example: /currency 1 eur usd
\nUse /warmon to display rashist casualty statistics for the day</b>
""",parse_mode="HTML")