from langgraph.graph import add_messages, MessagesState
from langchain_core.messages import AnyMessage, AIMessage, HumanMessage
from typing import TypedDict, Annotated

class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

# it is recommended to just inherit from MessageState as it is less verbose
# class MessagesState(MessagesState):
#     pass

initial_message = [AIMessage(content="Hello! How can I assist you?", name="Model"),
                   HumanMessage(content="I am looking for information on marinee biology.", name="Ewen")]
new_message = AIMessage(content="Hello! How can I assist you?", name="Model")

messages = add_messages(initial_message, new_message)
print(messages)