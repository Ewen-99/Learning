import os
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv('DASHSCOPE_API_KEY'),
    base_url = 'https://ws-wfwov01zm1nrkzlx.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1'
)

completion = client.chat.completions.create(
  model="qwen-flash-character",
  temperature = 1.5,
  messages=[
    {"role": "user", "content": "Hello! Tell me a fun fact about AI."}
  ]
)

print(completion.choices[0].message.content)