from ddgs import DDGS
import json


def web_search(query: str, num_results: int) -> str:
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
