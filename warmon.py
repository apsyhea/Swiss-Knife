import aiohttp
import datetime
import flag
from aiogram.types import Message

tz_offset: datetime.timedelta = datetime.timedelta(seconds=7200)
utc_time: datetime.datetime = datetime.datetime.utcnow()
print(utc_time)
local_time: datetime.datetime = utc_time + tz_offset


async def warmon(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://russianwarship.rip/api/v2/statistics/latest") as response:
            if response.status != 200:
                await message.reply("Sorry, something went wrong. Server API temporarily May not be available.")
                return

            data: dict = await response.json()

    stats: dict = data['data']['stats']
    stats_str: str = f"• Personnel Units: {stats['personnel_units']}\n"
    stats_str += f"• Tanks: {stats['tanks']}\n"
    stats_str += f"• Armoured Fighting Vehicles: {stats['armoured_fighting_vehicles']}\n"
    stats_str += f"• Artillery Systems: {stats['artillery_systems']}\n"
    stats_str += f"• MLRS: {stats['mlrs']}\n"
    stats_str += f"• AA Warfare Systems: {stats['aa_warfare_systems']}\n"
    stats_str += f"• Planes: {stats['planes']}\n"
    stats_str += f"• Helicopters: {stats['helicopters']}\n"
    stats_str += f"• Vehicles Fuel Tanks: {stats['vehicles_fuel_tanks']}\n"
    stats_str += f"• Warships Cutters: {stats['warships_cutters']}\n"
    stats_str += f"• Cruise Missiles: {stats['cruise_missiles']}\n"
    stats_str += f"• UAV Systems: {stats['uav_systems']}\n"
    stats_str += f"• Special Military Equip: {stats['special_military_equip']}\n"
    stats_str += f"• ATGM/SRBM Systems: {stats['atgm_srbm_systems']}\n"
    start_str: str = '========RASHISTS=LOSSES========'
    finish_str: str = '================================'

    await message.reply(f'<b> {flag.flag("UA")} On {local_time:%Y-%m-%d} | {local_time:%H:%M:%S}\n\n{start_str}\n{stats_str}{finish_str}\n🔪 Our russophobia is not enough\n💻 Dev: @apsyhea</b>', parse_mode="HTML")
