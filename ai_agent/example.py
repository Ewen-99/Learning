import json
from openai import OpenAI

client = OpenAI()   # reads OPENAI_API_KEY from your environment


# -------------------------------------------------------------
# The tool — a normal Python function (REAL, not mock)
# -------------------------------------------------------------
def get_weather(city: str) -> str:
    fake_db = {"beijing": "Sunny, 25°C", "london": "Rainy, 12°C", "tokyo": "Cloudy, 18°C"}
    return fake_db.get(city.lower(), f"No weather data for {city}.")


# Whitelist: LLM string name -> real Python function (REAL)
TOOL_FUNCTIONS = {"get_weather": get_weather}


# Schema the LLM sees (REAL — same shape OpenAI expects)
TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a given city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "e.g. 'Tokyo'"}
            },
            "required": ["city"],
        },
    },
}


# -------------------------------------------------------------
# The agent loop (REAL)
# -------------------------------------------------------------
def run_agent(user_input, max_steps=5):
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use tools when needed."},
        {"role": "user",   "content": user_input},
    ]

    for step in range(max_steps):
        # --- 1. Ask the real LLM ------------------------------
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=[TOOL_SCHEMA],
        )
        msg = response.choices[0].message        # the assistant's reply object

        # --- 2. If the LLM answered directly, we're done ------
        if not msg.tool_calls:                   # no tool requested
            return msg.content

        # --- 3. Otherwise, the LLM requested tool call(s) -----
        #     First, append the assistant's message (with tool_calls)
        #     so the conversation stays valid for the next API call.
        messages.append(msg)

        #     Run each requested tool
        for tc in msg.tool_calls:
            name = tc.function.name
            args = json.loads(tc.function.arguments)
            result = TOOL_FUNCTIONS[name](**args)

            #     Append the tool result, tagged with the matching id
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": str(result),
            })

        # Loop again — the LLM now sees the tool result and can answer.

    return "Stopped: max steps reached."


if __name__ == "__main__":
    print(run_agent("What's the weather in Tokyo?"))
