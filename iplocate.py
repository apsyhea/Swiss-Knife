import requests
from aiogram.types import Message
from dt import time, today

async def iplocate(message: Message):

    ip_addres = message.get_args()

    url = f'http://ip-api.com/json/{ip_addres}'
    response = requests.get(url)
    if response.status_code != 200:
        await message.reply("Sorry, something went wrong. Server API temporarily May not be available.")
        return
    
    date = response.json()
    date_str = f"Country Code: {date['countryCode']}\n"
    date_str += f"Country: {date['country']}\n"
    date_str += f"Region: {date['region']}\n"
    date_str += f"City: {date['city']}\n"
    date_str += f"Zip Code: {date['zip']}\n"
    date_str += f"Timezone: {date['timezone']}\n"
    date_str += f"Latitude: {date['lat']}\n"
    date_str += f"Longitude: {date['lon']}\n"
    date_str += f"Isp Provider: {date['isp']}\n"
    date_str += f"Organization: {date['org']}"

    await message.reply(f'<b>🕐 {time}\n🗓 {today}\n\n🗺 About ip address:\n\n<i>{date_str}</i></b>', parse_mode="HTML")