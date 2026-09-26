
WEATHER_SCHEMA = {
    'type': 'function',
    'function': {
        'name': 'weather',
        'description': 'get the weather of a specified time',
        'parameters': {
            'type': 'object',
            'properties': {
                'time': {'type':'string', 'description': "Only include four digit '00:00' for search, e.g. 13:00, 07:30"}
            }
        },
        'required': ['time']
    }
}

def weather(time):
    if time == '07:00':
        return 'sunny'
    if time == '08:00':
        return 'cloudy'
    else:
        return 'rainy'