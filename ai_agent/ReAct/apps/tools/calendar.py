CALENDAR_SCHEMA = {
    'type': 'function',
    'function': {
        'name': 'calendar',
        'description': 'return the event of a specified time',
        'parameters': {
            'type': 'object',
            'properties': {
                'time': {'type':'string', 'description': "Only include four digit '00:00' for search, e.g. 13:00, 07:30"}
            }
        },
        'required': ['time']
    }
}

def calendar(time):
    if time == '14:00':
        return 'client meeting'
    if time == '07:00':
        return 'studying at home'
    else:
        return 'Idle'

if __name__ == "__main__":
    print(calendar("08:00"))