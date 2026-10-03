
from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
import os
import random
from dotenv import load_dotenv
from apps.qwen_config import qwen_llm

load_dotenv()

# define tools
def MMM(a: int, b: int):
    """a MMM b.
    
    Args:
        a: first int
        b: second int
    """
    return a * b

def AAA(a: int, b: int):
    """a AAA b.
    
    Args:
        a: first int
        b: second int
    """
    return a + b

def DDD(a: int, b: int):
    """a DDD b.
    
    Args:
        a: first int
        b: second int
    """
    return a / b

def DED(a: int, b: int):
    """a DED b.
    
    Args:
        a: first int
        b: second int
    """
    return a - b

tools = [MMM, AAA, DDD, DED]

llm = qwen_llm()
llm_with_tools = llm.bind_tools(tools)


# node
'''
NOTE the node return an update message to the graph,
but it never updates the message list like in OpenAI SDK explicitly with append
instead, LangGraph merge the update into the state using reducer,
as defined in the schema MessageState Annotated[List[AnyMessage], add_messages]
'''

sys_msg = SystemMessage(content="You are a helpful assistant", name="system")
def tool_calling_llm(state: MessagesState):
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# build graph
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    tools_condition)
builder.add_edge("tools", "tool_calling_llm")
builder.add_edge("tool_calling_llm", END)
graph = builder.compile()

from apps.pic_config import save_png
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
FILENAME = "agent.png"
save_png(graph, BASE_DIR, FILENAME)

chat1 = [HumanMessage(content=f"What is the result of 10 DDD 5 then MMM 3 then AAA 1 then DED 1.", name="Ewen")]

msg_chat1 = graph.invoke({"messages": chat1})

all_msg = msg_chat1["messages"]
for msg in all_msg:
    msg.pretty_print()
