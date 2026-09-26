import json
import os
import logging
from .memory import summarize_messages, load_memory, save_memory

def run_ai(
        question,
        client,
        model, 
        tools: dict = {},
        tool_schema: list = []):

    # ReAct system message to define structural output
    system_prompt =  """
    You are a helpful assistant. 
    Please answer user's questions in short.

    Use the ReAct pattern for each question, you MUST:
    1. Thought: You must always first reason briefly about what to do next and respond, before using any tool.
    2. Action: call a tool if needed.
    3. Observation: after each tool call, capture the result returned by a tool.
    """
    messages = [
        {'role':'system', 'content': system_prompt}
        ]

    # Attach memory with user question
    memory = load_memory()
    messages.append({
        'role':'user',
        'content': f'Memory from past conversation: {memory}, \nQuestion: {question}'
        })

    logging.info('--- Chat with LLM Starts ---')
    logging.info(f'ROLE: user, QUESTION: {question}')
    print(question)

    # TODO trimming message length (potentially dangerous)
    max_length = 5
    if len(messages) > max_length:
        messages = [messages[0]] + messages[-(max_length-1):]

    while True:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tool_schema
        )
        choice = completion.choices[0]
        msg = choice.message
        messages.append({"role": "assistant", "content": msg.content})

        # 1) Reasoning
        if msg.content:
            logging.info(f'THOUGHT: {msg.content}')
            print(f'Thought: {msg.content}')

        # 2) Finish 
        if choice.finish_reason == 'stop' and not msg.tool_calls:
            logging.info(f'ROLE: {msg.role}, FINAL: {msg.content}')
            print(f'ROLE: {msg.role}, Final Answer: {msg.content}')

            mem = {'question': question, 'summary': summarize_messages(messages)}
            memory.append(mem)
            save_memory(memory)

            break

        # 3) Tool call        
        if msg.tool_calls:
            for tc in msg.tool_calls:
                name = tc.function.name
                args = json.loads(tc.function.arguments)
                result = tools[name](**args)

                messages.append({
                    'role': 'tool',
                    'tool_call_id': tc.id,
                    'content': str(result)
                })

                logging.info(f'ROLE: {msg.role}, ACTION: {name} {args} -> OBSERVATION: {result}')
                print(f'ROLE: {msg.role}, ACTION: {name} {args} -> OBSERVATION: {result}')


if __name__ == "__main__":
    print('main')
