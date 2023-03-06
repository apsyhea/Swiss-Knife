import json
import aiohttp
import asyncio
from aiogram import types
from aiogram.types import ParseMode


# Load blocklist from API
async def load_blocklist():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://uablacklist.net/all.json") as response:
            data = await response.text()
    return json.loads(data)

async def main():
    blocklist = await load_blocklist()
#    print(blocklist)

asyncio.run(main())


# Check if a given IP or URL is in the blocklist
async def is_blocked(ip_or_url):
    for item in blocklist:
        
        if ip_or_url in item["ips"] or ip_or_url in item["urls"]:
            return item
        
    return None

# Handle /blocklist command

async def blocklist(message: types.Message):
    text = message.text.replace("/blocklist ", "")
    item = await is_blocked(text)
    if item:
        # Display blocklist info
        alias = item["alias"]
        term = item["term"]
        urls = "\n".join(item["urls"])
        ips = "\n".join(item["ips"])
        msg = f"<b>{alias}</b> is blocked in Ukraine until {term}.\n\nURLs:\n{urls}\n\nIPs:\n{ips}"
        await message.reply(msg, parse_mode=ParseMode.HTML)
    else:
        # Display not blocked message
        msg = f"{text} is not blocked in Ukraine."
        await message.reply(msg)
