from ddgs import DDGS
import json


def web_search(query: str, num_results: int = 3) -> str:
    results = []
    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(query, max_results=num_results)
            for result in search_results:
                results.append(
                    {
                        "title": result["title"],
                        "href": result["href"],
                        "body": result["body"],
                    }
                )
    except Exception as e:
        print(f"Error performing web search: {e}")
    if not results:
        return "No search results found."

    formatted = f"search result for: {query}\n"
    for i, result in enumerate(results):
        formatted += "\n"
        formatted += f"Result {i + 1}:\n"
        formatted += f"Title: {result['title']}\n"
        formatted += f"URL: {result['href']}\n"
        formatted += f"Summary: {result['body']}\n"
        formatted += "\n"
    return formatted.strip()


web_search_tool = {
    "type": "function",
    "function": {
        "name": "web_search",
        "description": "Search the web for current information, recent events, or facts not in the model's training data. "
        "Always use this tool when the question requires up-to-date or external knowledge.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "The precise search query"},
                "num_results": {
                    "type": "integer",
                    "description": "Number of results to return (1-5 recommended)",
                    "default": 3,
                },
            },
            "required": ["query"],
        },
    },
}

available_tools = [web_search_tool]

tool_handler = {"web_search": web_search}
