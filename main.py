from agent import client, DEFAULT_MODEL


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


if __name__ == "__main__":
    test_connection()
