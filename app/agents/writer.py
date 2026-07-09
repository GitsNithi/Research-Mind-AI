from app.llm import llm

def writer_agent(topic: str, summary: str):
    prompt = f"""
    You are a professional research report writer.

    Write a well-structured report.

    Topic:
    {topic}

    Summary:
    {summary}

    Format:

    # Title

    ## Introduction

    ## Key Findings

    ## Conclusion

    Keep the report professional and easy to read.
    """

    response = llm.invoke(prompt)

    return response.content