from app.tools.search_tool import search_tool


def search_agent(query: str):
    return search_tool.invoke({"query": query})