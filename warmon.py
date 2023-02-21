import requests
from aiogram.types import Message
from dt import time, today

async def warmon(message: Message):

    url = 'https://russianwarship.rip/api/v2/statistics/latest'
    response = requests.get(url)
    if response.status_code != 200:
        await message.reply("Sorry, something went wrong. Server API temporarily May not be available.")
        return

    data = response.json()
    stats = data['data']['stats']
    stats_str = f"• Personnel Units: {stats['personnel_units']}\n"
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

    await message.reply(f'<b>🗓 {today}\n\n🐷 Total combat losses of the russian pigs:\n<i>{stats_str}</i>\n💻 Dev: @apsyhea</b>', parse_mode="HTML")