import aiohttp
import flag
from aiogram.types import Message
from .messages import msg_emoji, msg_iplocate


async def iplocate(message: Message) -> None:
    ip_address: str | None = message.get_args()
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
            date_str += f"{msg_emoji['region']} {msg_iplocate['region']} {json_response['region']}\n"
            date_str += f"{msg_emoji['city']} {msg_iplocate['city']} {json_response['city']}\n"
            date_str += f"{msg_emoji['zip']} {msg_iplocate['zip']} {json_response['zip']}\n"
            date_str += f"{msg_emoji['tz']} {msg_iplocate['tz']} {json_response['timezone']}\n"
            date_str += f"{msg_emoji['lat']} {msg_iplocate['lat']} {json_response['lat']}\n"
            date_str += f"{msg_emoji['lon']} {msg_iplocate['lon']} {json_response['lon']}\n"
            date_str += f"{msg_emoji['isp']} {msg_iplocate['isp']} {json_response['isp']}\n"
            date_str += f"{msg_emoji['org']} {msg_iplocate['org']} {json_response['org']}\n"
            date_str += f"{msg_emoji['ip']} {msg_iplocate['ip']} {json_response['query']}"

            await message.reply(f'<b>{date_str}\n\n💻 Dev: @apsyhea</b>', parse_mode="HTML")
