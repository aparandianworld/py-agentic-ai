from ddgs import DDGS
import json


def web_search(query: str, num_results: int) -> str:
    results = []
    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(query, max_results=num_results)
            for result in search_results:
                results.append(result)
    except Exception as e:
        print(f"Error performing web search: {e}")
    if not results:
        return "No search results found."

    return json.dumps(results)
