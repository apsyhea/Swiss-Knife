"""
This package contains modules for various functionalities.

Modules:
- messages: Defines a set of messages that can be used throughout the application.
- warmon: Displays the losses of the Russian army in Ukraine.
- weather: Retrieves weather information for a given location using OpenWeatherMap API.
- currency: Provides currency conversion functionality using Open Exchange Rates API.
- iplocate: Retrieves the geographical location of an IP address using ipapi API.
- alarm: Displays air alert in Ukraine.
"""
import modules.messages as messages
from modules.warmon import warmon
from modules.weather import weather
from modules.currency import currency
from modules.iplocate import iplocate
from modules.alarm import alarm
from modules.blocklist import blocklist
