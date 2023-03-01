import datetime
import flag
import json
import aiohttp
from tokens import alarm_token
from aiogram.types import Message


A_TOKEN = alarm_token

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
            tz_offset = datetime.timedelta(seconds=7200)
            utc_time = datetime.datetime.utcnow()
            local_time = utc_time + tz_offset
            time = f'{local_time:%Y-%m-%d} | {local_time:%H:%M:%S}'
            country_flag = flag.flag('UA')
            state = json.loads(data)
            for alarm_state in state['states']:
                if alarm_state['alert']:
                    alert_names.append(alarm_state['name_en'])
                    alarm_state['changed'] = alarm_state.get('changed', '')  # add 'changed' field if not present
            if alert_names:
                alarm_info = "\n🚨 ".join(alert_names)
                await message.reply(f"<b>{country_flag} {time}\n⚠️ Air alarm:\n🚨 {alarm_info}\n\n💻 Dev: @apsyhea</b>", parse_mode='HTML')
