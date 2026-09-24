import os
import json
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv('DASHSCOPE_API_KEY'),
    base_url = 'https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1'
)


def get_weather(city: str) -> str:
    fake_db = {"beijing": "Sunny, 25°C", "london": "Rainy, 12°C", "tokyo": "Cloudy, 18°C"}
    return fake_db.get(city.lower(), f"No record for {city}.")

TOO_FUNCTIONS = {"get_weather": get_weather}

TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather of a city",
        "parameters":{
            "type":"object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "e.g. Beijing"
                }
            },
            "required": "city"
        }
    }
}


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the weather in Tokyo?"}
]

response = client.chat.completions.create(
    model = "qwen3.6-flash",
    messages = messages,
    tools = [TOOL_SCHEMA]
)
choice = response.choices[0]
msg = choice.message


