import re
import aiohttp
from aiogram import types


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def get_json_data():
    url = "https://uablacklist.net/all.json" # заменить на URL нужного API
    json_data = await fetch_json(url)
    return json_data


async def blocklist(message: types.Message) -> None:
    json_data = await get_json_data()
    query: str | None = message.get_args()
    is_blocked = False
    
    for data in json_data.values():
        urls: list[Any] = [url.rstrip('/') for url in data['urls']]
        ips = data['ips']
        

        if any(re.search(query, url) for url in urls) or query in ips:
            is_blocked = True
            await message.reply(f"{query} IP address blocked on the territory of Ukraine")
            break
    
    if not is_blocked:
        await message.reply(f"{query} IP address is not blocked on the territory of Ukraine")