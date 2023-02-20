import requests
import datetime
from aiogram.types import Message

async def warmon(message: Message):

    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')
    url = f'https://russianwarship.rip/api/v2/statistics?offset=0&limit=50&date_from={date_str}&date_to={date_str}'

    response = requests.get(url)
    data = response.json()

    stats = data['data']['records'][0]['stats']
    stats_str = f"Personnel Units: {stats['personnel_units']}\n"
    stats_str += f"Tanks: {stats['tanks']}\n"
    stats_str += f"Armoured Fighting Vehicles: {stats['armoured_fighting_vehicles']}\n"
    stats_str += f"Artillery Systems: {stats['artillery_systems']}\n"
    stats_str += f"MLRS: {stats['mlrs']}\n"
    stats_str += f"AA Warfare Systems: {stats['aa_warfare_systems']}\n"
    stats_str += f"Planes: {stats['planes']}\n"
    stats_str += f"Helicopters: {stats['helicopters']}\n"
    stats_str += f"Vehicles Fuel Tanks: {stats['vehicles_fuel_tanks']}\n"
    stats_str += f"Warships Cutters: {stats['warships_cutters']}\n"
    stats_str += f"Cruise Missiles: {stats['cruise_missiles']}\n"
    stats_str += f"UAV Systems: {stats['uav_systems']}\n"
    stats_str += f"Special Military Equip: {stats['special_military_equip']}\n"
    stats_str += f"ATGM/SRBM Systems: {stats['atgm_srbm_systems']}\n"

    await message.reply(stats_str)