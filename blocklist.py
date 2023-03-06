import json
import aiohttp
from aiogram import types
from aiogram.types import ParseMode


async def load_blocklist():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://uablacklist.net/all.json") as response:
            data = await response.text()
    return json.loads(data)


async def is_blocked(ip_or_url):
    blocklist = await load_blocklist()
    for item in blocklist:
        if isinstance(item, dict) and (ip_or_url in item["ips"] or ip_or_url in item["urls"]):
            return item
    return None


async def blocklist(message: types.Message):
    text = message.get_args()
    item = await is_blocked(text)
    if item:
        alias = item["alias"]
        term = item["term"]
        urls = "\n".join(item["urls"])
        ips = "\n".join(item["ips"])
        msg = f"<b>{alias}</b> is blocked in Ukraine until {term}.\n\nURLs:\n{urls}\n\nIPs:\n{ips}"
        await message.reply(msg, parse_mode=ParseMode.HTML)
    else:
        msg = f"{text} is not blocked in Ukraine."
        await message.reply(msg)
