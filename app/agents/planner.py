from app.llm import llm


def planner_agent(topic: str):
    prompt = f"""
    You are an expert research planner.

    Break the following topic into 5-7 research objectives.

    Topic:
    {topic}

    Return only the numbered objectives.
    """

    response = llm.invoke(prompt)
    return response.content