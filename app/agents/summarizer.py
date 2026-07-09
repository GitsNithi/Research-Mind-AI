from app.llm import llm


def summarizer_agent(notes):
    prompt = f"""
    You are an expert research analyst.

    Summarize the following research notes.

    Requirements:
    - Keep it concise.
    - Highlight key insights.
    - Use bullet points.
    - Remove duplicate ideas.

    Notes:

    {notes}
    """

    response = llm.invoke(prompt)

    return response.content