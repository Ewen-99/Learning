from .calendar import CALENDAR_SCHEMA, calendar
from .weather import WEATHER_SCHEMA, weather

TOOL_SCHEMA =[CALENDAR_SCHEMA, WEATHER_SCHEMA]
TOOLS = {'calendar': calendar, 'weather': weather}
