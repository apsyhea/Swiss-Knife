msg_start: str = """
<b>Hello, I'm a Swiss Knife bot. 
\nTo display the current weather 
input: /weather [city] 
For example <code>/weather Tokyo</code>
\nTo convert the exchange rate 
input: /currency [number][currency][currency]
For example:  <code>/currency 1 eur usd</code>
\nFind out the geo and provider ip address:
input: /iplocate [ip address]
For example: <code>/iplocate 8.8.8.8</code>
\nUse /warmon to display rashist casualty statistics for the day</b>
\nUse /alarm to display air alarm in Ukraine
"""
msg_changelog: str = """
<b>Changelog 3.31.2023
Release version of the bot.
All available bot functions can be viewed with the /help command</b>

<b>What is implemented:</b>
<code>1. The weather module now displays the local time zone for the region you are requesting weather for.
2. In the Iplocate module, you can now specify DNS (note. github .com)
3. In the currency module, the amount value is rounded to 2 decimal places after zero. (note. 1.0 UAH is 0.03 USD)
4. The alarm module requires API optimization, so the result may not return the first time.</code>

<b>🪢 Github: https://github.com/apsyhea/Swiss-Knife
💻 Dev: @apsyhea</b>
"""
# msg_help = ''
"""
msg_weather: dict =  {
    'day': '🌤️',
    'temperature': '🌡️',
    'description': '☁️',
    'wind_speed': '💨',
}
"""
msg_iplocate: dict = {
    'country': 'Country:',
    'region': 'Region:',
    'city': 'City:',
    'zip': 'Zip Code:',
    'tz': 'Timezone:',
    'lat': 'Latitude:',
    'lon': 'Longitude:',
    'isp': 'Isp Provider:',
    'org': 'Organization:',
    'ip': 'IP Address:',
}


msg_emoji: dict = {
    'region': '🗺',
    'city': '🌆',
    'zip': '✉️',
    'tz': '🕐',
    'lat': '📍',
    'lon': '📍',
    'isp': '🌐',
    'org': '🏢',
    'ip': '🖥',
}

