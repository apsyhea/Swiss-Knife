import json
import flag
import aiohttp
import modules
from aiogram.types import Message
from typing import List
from config import alarm_token

A_TOKEN: str = alarm_token

async def alarm(message: Message) -> None:
    local_time = modules.get_data()
    url: str = 'https://alerts.com.ua/api/states'
    headers: dict = {'X-API-Key': f'{A_TOKEN}'}
    alert_names: List[str] = []
    start_str = '------------------------\n'
    finish_str = '\n------------------------'

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                await message.reply("Sorry, something went wrong. Server API temporarily May not be available.")
                return
            data: str = await response.text()
            state: dict = json.loads(data)
            for alarm_state in state['states']:
                if alarm_state['alert']:
                    alert_names.append(alarm_state['name_en'])
                    alarm_state['changed'] = alarm_state.get('changed', '')
                    alarm_info: str = "\n ".join(alert_names)
                    alarm_info += finish_str
            if alert_names:
                await message.reply(f'<b>{flag.flag("UA")} {local_time:%Y-%m-%d}\n🚨 Air alarm:\n<code>{start_str} {alarm_info}</code>\n\n💻 Dev: @apsyhea\n</b>', parse_mode="HTML")


