import aiohttp
import flag
from aiogram.types import Message


async def iplocate(message: Message) -> None:
    ip_address: str = message.get_args()
    if not ip_address:
        await message.reply('Please enter an IP address or domain. Try /help', parse_mode='HTML')
        return

    async with aiohttp.ClientSession() as session:
        url: str = f'http://ip-api.com/json/{ip_address}'
        async with session.get(url) as response:
            if response.status != 200:
                await message.reply("Sorry, something went wrong. Server API temporarily May not be available.")
                return
            json_response: dict = await response.json()
            if json_response['status'] == 'fail':
                await message.reply(f"This address in {json_response['message']}")
                return

            date_str: str = f"{flag.flag(json_response['countryCode'])}"
            date_str += f" Country: {json_response['country']}\n"
            date_str += f"🗺 Region: {json_response['region']}\n"
            date_str += f"🌆 City: {json_response['city']}\n"
            date_str += f"✉️ Zip Code: {json_response['zip']}\n"
            date_str += f"🕐 Timezone: {json_response['timezone']}\n"
            date_str += f"📍 Latitude: {json_response['lat']}\n"
            date_str += f"📍 Longitude: {json_response['lon']}\n"
            date_str += f"🌐 Isp Provider: {json_response['isp']}\n"
            date_str += f"🏢 Organization: {json_response['org']}\n"
            date_str += f"🖥 IP Address {json_response['query']}"

            await message.reply(f'<b>{date_str}\n\n💻 Dev: @apsyhea</b>', parse_mode="HTML")

