import aiohttp
import modules
import flag
from aiogram.types import Message


async def warmon(message: Message) -> None:
    local_time = modules.get_data()
    async with aiohttp.ClientSession() as session:
        async with session.get("https://russianwarship.rip/api/v2/statistics/latest") as response:
            if response.status != 200:
                await message.reply("Sorry, something went wrong. Server API temporarily May not be available.")
                return

            data: dict = await response.json()

    stats: dict = data['data']['stats']
    stats_str: str = f"    • Personnel Units: {stats['personnel_units']}\n"
    stats_str += f"    • Tanks: {stats['tanks']}\n"
    stats_str += f"    • Armoured Vehicles: {stats['armoured_fighting_vehicles']}\n"
    stats_str += f"    • Artillery Systems: {stats['artillery_systems']}\n"
    stats_str += f"    • MLRS: {stats['mlrs']}\n"
    stats_str += f"    • AA Warfare Systems: {stats['aa_warfare_systems']}\n"
    stats_str += f"    • Planes: {stats['planes']}\n"
    stats_str += f"    • Helicopters: {stats['helicopters']}\n"
    stats_str += f"    • Vehicles Fuel Tanks: {stats['vehicles_fuel_tanks']}\n"
    stats_str += f"    • Warships Cutters: {stats['warships_cutters']}\n"
    stats_str += f"    • Cruise Missiles: {stats['cruise_missiles']}\n"
    stats_str += f"    • UAV Systems: {stats['uav_systems']}\n"
    stats_str += f"    • Special Military Equip: {stats['special_military_equip']}\n"
    stats_str += f"    • ATGM/SRBM Systems: {stats['atgm_srbm_systems']}\n"
    header_str: str = 'Rashist loses:'
    start_str: str =  '┏━━━━━━━━━━━━━━━━━━┓'
    finish_str: str = '┗━━━━━━━━━━━━━━━━━━┛'

<<<<<<< HEAD

    await message.reply(f'<b> {flag.flag("UA")} On {local_time:%Y-%m-%d} | {local_time:%H:%M:%S}\n🗑 {header_str}\n\n\
=======
    await message.reply(f'<b> {flag.flag("UA")} On {local_time:%Y-%m-%d}\n🗑 {header_str}\n\n\
>>>>>>> a314ffb (tzdata)
{start_str}\n{stats_str}{finish_str}\n\n\
🔪 Our russophobia is not enough\n💻 Dev: @apsyhea</b>', parse_mode="HTML")
