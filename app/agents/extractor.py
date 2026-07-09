from app.llm import llm


def extractor_agent(search_results):
    prompt = f"""
    You are a research assistant.

    Extract only the important information from these search results.

    Ignore advertisements, navigation menus,
    unrelated content and repeated information.

    Return clean research notes.

    Search Results:

    {search_results}
    """

    response = llm.invoke(prompt)

    return response.content