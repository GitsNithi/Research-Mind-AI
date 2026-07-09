from langgraph.graph import StateGraph, START, END

from app.graph.state import ResearchState

from app.agents.planner import planner_agent
from app.agents.search import search_agent
from app.agents.extractor import extractor_agent
from app.agents.summarizer import summarizer_agent
from app.agents.writer import writer_agent

def planner_node(state: ResearchState):
    plan = planner_agent(state["topic"])
    return {"plan": plan}


def search_node(state: ResearchState):
    results = search_agent(state["topic"])
    return {"search_results": results}


def extractor_node(state: ResearchState):
    notes = extractor_agent(state["search_results"])
    return {"notes": notes}


def summarizer_node(state: ResearchState):
    summary = summarizer_agent(state["notes"])
    return {"summary": summary}


def writer_node(state: ResearchState):
    report = writer_agent(state["topic"], state["summary"])
    return {"report": report}

builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("search", search_node)
builder.add_node("extractor", extractor_node)
builder.add_node("summarizer", summarizer_node)
builder.add_node("writer", writer_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", "search")
builder.add_edge("search", "extractor")
builder.add_edge("extractor", "summarizer")
builder.add_edge("summarizer", "writer")
builder.add_edge("writer", END)

graph = builder.compile()