
from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
import os
import random

from apps.qwen_config import qwen_llm

# define tools
def multiply(a: int, b: int):
    """Multiply a and b and a random number.
    
    Args:
        a: first int
        b: second int
    """
    return a * b * random.randint(1, 100)

llm = qwen_llm()
llm_with_tools = llm.bind_tools([multiply])


# node
'''
NOTE the node return an update message to the graph,
but it never updates the message list like in OpenAI SDK explicitly with append
instead, LangGraph merge the update into the state using reducer,
as defined in the schema MessageState Annotated[List[AnyMessage], add_messages]
'''
def tool_calling_llm(state: MessagesState):
    # return {"messages": "testing: no message in the node"}
    return {"messages": [llm_with_tools.invoke(state["messages"])]} # NOTE llm call takes place with this invoke

# build graph
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode([multiply]))
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    tools_condition)
builder.add_edge("tools", END)
graph = builder.compile()

from apps.pic_config import save_png
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
FILENAME = "router.png"
save_png(graph, BASE_DIR, FILENAME)

chat1 = [HumanMessage(content=f"What is the result of 2 multiply by 3 and a random number.", name="Ewen")]
chat2 = [HumanMessage(content=f"What is the capital city of France?", name="Ewen")]

msg_chat1 = graph.invoke({"messages": chat1})   # NOTE LLM call is NOT initiated here. This invoke only kicks off the udpates of graph states
msg_chat2 = graph.invoke({"messages": chat2})   # NOTE the actual running of LLM is invoked in the node

all_msg = msg_chat1["messages"] + msg_chat2["messages"]
for msg in all_msg:
    msg.pretty_print()
