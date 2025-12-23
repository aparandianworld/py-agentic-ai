from openai import OpenAI
from utils import get_openai_api_key
from tools import available_tools, tool_handler
import json


DEFAULT_MODEL = "gpt-4o-mini"

client = OpenAI(api_key=get_openai_api_key())
if client is None:
    raise ValueError("Failed to create OpenAI client")
print("OpenAI client created successfully")


def run_agent(query: str, max_iteration: int = 5):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Use the provided tools when you need up to date information or external knowledge. This step by step and provide a clear, structured final answer.",
        },
        {"role": "user", "content": query},
    ]

    turns = 0
    while turns <= max_iteration:
        turns += 1

        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=messages,
            tools=available_tools,
            tool_choice="auto",
        )

        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            print(f"Tool calls detected: {message.tool_calls}")
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                print(f"Calling function: {function_name} with args: {function_args}")

                if function_name in tool_handler:
                    function_response = tool_handler[function_name](**function_args)

                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": function_response,
                        }
                    )
        else:
            print(f"No tool calls in this response.")
            final_answer = message.content.strip()
            return final_answer

    return "Max iterations reached without a final answer."
