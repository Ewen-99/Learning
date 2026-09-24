import os
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv('QWEN_API_KEY'),
    base_url = os.getenv('QWEN_BASE_URL')
)

MODEL = "qwen3.6-flash"

completion = client.chat.completions.create(
  model=MODEL,
  temperature = 1.5,
  messages=[
    {"role": "user", "content": "Hello! Tell me a fun fact about AI."}
  ]
)

print(completion.choices[0].message.content)