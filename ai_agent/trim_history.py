import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import logging

logging.basicConfig(filename='test.log', level=logging.INFO)

load_dotenv()
client = OpenAI(
    api_key=os.getenv('QWEN_API_KEY'),
    base_url=os.getenv('QWEN_BASE_URL')
)

MODEL = "qwen3.6-flash"

# tool schema
CALENDAR_SCHEMA = {
    'type': 'function',
    'function': {
        'name': 'calendar',
        'description': 'return the event of a specified time',
        'parameters': {
            'type': 'object',
            'properties': {
                'time': {'type':'str', 'description': "Only include four digit '00:00' for search, e.g. 13:00, 07:30"}
            }
        },
        'required': 'time'
    }
}

WEATHER_SCHEMA = {
    'type': 'function',
    'function': {
        'name': 'weather',
        'description': 'get the weather of a specified time',
        'parameters': {
            'type': 'object',
            'properties': {
                'time': {'type':'str', 'description': "Only include four digit '00:00' for search, e.g. 13:00, 07:30"}
            }
        },
        'required': 'time'
    }
}

TOOL_SCHEMA =[CALENDAR_SCHEMA, WEATHER_SCHEMA]

# tool function
def calendar(time):
    if time == '14:00':
        return 'client meeting'
    if time == '07:00':
        return 'studying at home'
    else:
        return 'Idle'

def weather(time):
    if time == '15:00':
        return 'rainy'
    if time == '08:00':
        return 'sunny'
    else:
        return 'cloudy'

# tool list
TOOLS = {'calendar': calendar, 'weather': weather}

# while loop
def run_ai(questions):
    messages = [
        {'role':'system', 'content': '''help me figure out when i can go out. 
        i can only go out when the weather is sunny and i am idle.'''}
        ]

    logging.info('--- Chat with LLM Starts ---')

    for q in questions:

        logging.info(f'QUESTION: {q}')
        # print(q)

        # trimming message length
        max_length = 5
        # print(len(messages))
        if len(messages) > max_length:
            messages = [messages[0]] + messages[-(max_length-1):]

        messages.append({'role':'user', 'content': q})

        while True:
            completion = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=TOOL_SCHEMA
            )
            choice = completion.choices[0]
            msg = choice.message
            messages.append(msg)

            logging.info(f'LLM: {msg}')

            if choice.finish_reason == 'stop':
                logging.info(f'FINAL: {msg.content}')
                break
                        
            if msg.tool_calls:
                for tc in msg.tool_calls:
                    name = tc.function.name
                    args = json.loads(tc.function.arguments)
                    result = TOOLS[name](**args)

                    messages.append({
                        'role': 'tool',
                        'tool_call_id': tc.id,
                        'content': str(result)
                    })

                    logging.info(f'TOOL CALL: {name} {args} -> {result}')
                # print(result)

# input question list
questions = [
    'Check my calendar at 14:00?',
    'Check if I can go out at 15:00?',
    'Check if I can go out at 7:00?',
    'Check if I can go out at 8:00?',
]

def main():
    run_ai(questions)

if __name__ == "__main__":
    main()

