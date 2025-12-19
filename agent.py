from openai import OpenAI
from utils import get_openai_api_key


DEFAULT_MODEL = "gpt-4o-mini"

client = OpenAI(api_key=get_openai_api_key())
if client is None:
    raise ValueError("Failed to create OpenAI client")
print("OpenAI client created successfully")
