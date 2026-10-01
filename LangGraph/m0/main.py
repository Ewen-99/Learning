from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from pydantic import SecretStr

load_dotenv()  # This reads the .env file and sets the variables

api_key = os.getenv("QWEN_API_KEY")
if not api_key:
    raise ValueError("api key is not set.")

base_url = os.getenv("QWEN_BASE_URL")
if not base_url:
    raise ValueError("base url is not set.")

llm = ChatOpenAI(
    model="qwen3.8-flash",
    base_url=base_url,
    api_key=SecretStr(api_key)
)
llm.invoke("Hello!")