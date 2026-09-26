import os
from .config import get_client, MODEL
import json
import logging

MEMORY_FILE = "memory.json"
MEMORY_MAX_LEN = 5

# TODO adopt a better memory management strategy
# TODO add a search memory strategy
def save_memory(memory: list):
    if len(memory) > MEMORY_MAX_LEN:
        logging.warning("Memory entries > 5, trimming memories")
        memory =  memory[-(MEMORY_MAX_LEN-1):]

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

def load_memory() -> list:
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:          
            return json.load(f)
    except:
        logging.warning("Memory file unreadable, start with empty memory.")
        return []

# transcripe single message
def _msg_to_text(m: dict) -> str:
    if isinstance(m, dict):
        role, content, tool_calls = m.get('role', ''), m.get('content', None), m.get('tool_calls', None)
        parts = [f"{role}:{content or ""}"]
        if tool_calls:
            for tc in tool_calls:
                parts.append(f"  tool call -> {tc.function.name}({tc.function.arguments})")
        return "\n".join(parts)
    else:
        return None

def summarize_messages(messages: list) -> str:
    transcript = "\n".join(_msg_to_text(m) for m in messages)

    if not transcript:
        return None
    
    prompt = (
    "Summarize the assistant's reasoning process below into ONE short paragraph "
    "(under 60 words). Include: the question, which tools were called with which "
    "arguments, the key observations, and the final answer.\n\n"
    f"{transcript}"
)
    client = get_client()
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {'role': 'system',
             'content': 'You compress agent trajectories into compact, factual memories.'},
             {'role': 'user', 'content': prompt}
        ],
    )
    return completion.choices[0].message.content.strip()



if __name__ == "__main__":    
    from openai.types.chat import ChatCompletionMessageFunctionToolCall
    from openai.types.chat.chat_completion_message_function_tool_call import Function

    # m = {'role':'assistant', 'tool_calls': [
    #     ChatCompletionMessageFunctionToolCall(id='call_52f105593ea94387a1f9c899', function=Function(arguments='{"time": "07:00"}', name='calendar'), type='function', index=0)
    # ]}
    # print(_msg_to_text(m))

    messages_1 = [
        {'role': 'system', 'content': 'you are a helpful weather search assistant.'},
        {'role': 'user', 'content': 'how is the weather today?'},
        {'role':'assistant', 'tool_calls': [
            ChatCompletionMessageFunctionToolCall(id='call_52f105593ea94387a1f9c899', function=Function(arguments='{"time": "07:00"}', name='weather_api_Meteo'), type='function', index=0)
        ]},
        {'role':'assistant', 'content': 'the weather is good.'}
        ]
    print(summarize_messages(messages_1))

    # messages_empty = None
    # print(summarize_messages(messages_empty))
