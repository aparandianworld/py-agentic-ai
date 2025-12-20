from agent import client, DEFAULT_MODEL
from tools import web_search


def test_connection():
    try:
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": "Say: 'Hello, research agent set up is working as expected.'",
                }
            ],
            max_tokens=10,
        )
        print(
            f"Test response from OpenAI: {response.choices[0].message.content.strip()}"
        )
    except Exception as e:
        print(f"Error testing connection: {e}")


def test_web_search():
    print("Testing web search tool...\n")
    response = web_search("What is the latest advancement on Agentic AI?", 1)
    if response:
        print(response)
    else:
        print("No response from web search tool.")


if __name__ == "__main__":
    test_connection()
    print("\n" + "-" * 25 + "\n")
    test_web_search()
