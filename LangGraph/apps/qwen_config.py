from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pydantic import SecretStr

MODEL="qwen3.8-flash"
BASE_URL = os.getenv("QWEN_BASE_URL")
API_KEY = SecretStr(os.getenv("QWEN_API_KEY") or "")

if not BASE_URL:
    raise ValueError("base url not set!")
if not API_KEY:
    raise ValueError("api key not set!")

def qwen_llm():
    return ChatOpenAI(
        model=MODEL,
        base_url=BASE_URL,
        api_key=API_KEY
    )