import os
import json
from openai import OpenAI
import json
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key = os.getenv('QWEN_API_KEY'),
    base_url = os.getenv('QWEN_BASE_URL')
)
MODEL = "qwen3.6-flash"

def get_weather(city: str) -> str:
    fake_db = {"beijing": "Sunny, 25°C", "london": "Rainy, 12°C", "tokyo": "Cloudy, 18°C"}
    return fake_db.get(city.lower(), f"No record for {city}.")

TOOL_FUNCTIONS = {"get_weather": get_weather}

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

def run_agent(user_input, max_step = 5):

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]

    for step in range(max_step):

        response = client.chat.completions.create(
            model = MODEL,
            messages = messages,
            tools = [TOOL_SCHEMA]
        )
        choice = response.choices[0]
        msg = choice.message

        if choice.finish_reason == "stop":
            return msg.content

        if msg.tool_calls:
            for tc in msg.tool_calls:
                name = tc.function.name
                args = json.loads(tc.function.arguments)
                result = TOOL_FUNCTIONS[name](**args)

            messages.append({
                "role": "tool", 
                "tool_call_id": tc.id,
                "content": str(result)
            })
            
    return "Stopped: max steps reached."
            

if __name__ == "__main__":
    print(run_agent("What's the weather in Tokyo?"))