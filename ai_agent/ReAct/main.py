from apps.run_ai import run_ai
from apps.tools import TOOL_SCHEMA, TOOLS
from apps.config import get_client, MODEL
import os
import logging
from pathlib import Path

# set up OpenAI clien67t object
# set model here in config.py
client = get_client()

# setup logging
BASE_DIR = Path(__file__).resolve().parent
log_dir = os.path.join(BASE_DIR, "logs")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, "ReAct.log"),
    level=logging.INFO)

# provide input and run model
questions = [
    # 'Can I go out at 07:00 or 08:00, check my schedules and the weather?',
    'How can AI help develop code better?',
    'How many hours are there in a day?',
    'How is the weather in Germany today?'
    'How is the weather in China today?'

]

for q in questions:
    run_ai(
        q, 
        client,
        model=MODEL,
        tools=TOOLS,
        tool_schema=TOOL_SCHEMA)

