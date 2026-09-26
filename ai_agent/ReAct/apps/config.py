from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
MODEL = "qwen3.8-flash"

def get_client():
    return OpenAI(
        api_key=os.getenv('QWEN_API_KEY'),
        base_url=os.getenv('QWEN_BASE_URL')
    )
