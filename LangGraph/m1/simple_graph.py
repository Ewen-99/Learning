from typing import TypedDict, Literal
import random
from langgraph.graph import StateGraph, START, END
from apps.pic_config import save_png
from pathlib import Path

# define state dict, with only one key
class State(TypedDict):
    graph_state: str

# define three nodes, they are just functions
def node_1(state):
    print("--- Node 1 ---")
    return {"graph_state": state["graph_state"] + "\nI am"}

def node_2(state):
    print("--- Node 2 ---")
    return {"graph_state": state["graph_state"] + " happy!"}

def node_3(state):
    print("--- Node 3 ---")
    return {"graph_state": state["graph_state"] + " sad!"}

# define conditional edges leading to node 2 and 3
def decide_mood(state) -> Literal["node_2", "node_3"]:
    user_input = state["graph_state"]
    return random.choice(["node_2", "node_3"])

# build a graph instance
builder = StateGraph(State) # pass in the schema of state dict to define a StateGraph instance
builder.add_node("node_1", node_1)  # setting up nodes in the graph, they are simply just functions
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_edge(START, "node_1")   # pass in the name of the node, not the actual variable
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)    # can't use decide_mood as it produces changable results everytime, just hardcode the connection between node2/3 and END
builder.add_edge("node_3", END)

graph = builder.compile()

# produce a IPython image
BASE_DIR = Path(__file__).resolve().parent
FILENAME = "simple_graph.png"
save_png(graph, BASE_DIR, FILENAME)

# image = Image(graph.get_graph().draw_mermaid_png())

# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent
# FILENAME = BASE_DIR / "simple_graph.png"
# with open(FILENAME, "wb") as f:
#     f.write(image.data)



# # graph invocation
# output = graph.invoke({"graph_state": "Hi this is Ewen"})
# print(output)