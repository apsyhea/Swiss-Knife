import json
import flag
import aiohttp
import datetime
import asyncio
from tokens import alarm_token
from aiogram.types import Message

A_TOKEN = alarm_token


async def send_notification(message: Message, alert_names: list):
    tz_offset = datetime.timedelta(seconds=7200)
    utc_time = datetime.datetime.utcnow()
    local_time = utc_time + tz_offset
    alarm_info = "\n🚨 ".join(alert_names)
    await message.reply(f"<b>{flag.flag('UA')} {local_time:%Y-%m-%d} | {local_time:%H:%M:%S}\n⚠️ Air alarm:\n🚨 {alarm_info}</b>", parse_mode='HTML')


async def alarm(message: Message):
    url = 'https://alerts.com.ua/api/states'
    headers = {'X-API-Key': f'{A_TOKEN}'}
    alert_names = []

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                await message.reply("Sorry, something went wrong. Server API temporarily May not be available.")
                return
            data = await response.text()
            state = json.loads(data)
            for alarm_state in state['states']:
                if alarm_state['alert']:
                    alert_names.append(alarm_state['name_en'])
                    alarm_state['changed'] = alarm_state.get('changed', '')
            if alert_names:
                await send_notification(message, alert_names)


async def alarm_scheduler(message: Message):
    while True:
        await alarm(message)
        await asyncio.sleep(101)


if __name__ == '__main__':
    asyncio.create_task(alarm_scheduler(message))
    executor.start_polling(dp, skip_updates=True)
