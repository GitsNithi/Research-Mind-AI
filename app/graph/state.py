from typing import TypedDict


class ResearchState(TypedDict):
    topic: str
    plan: str
    search_results: dict
    notes: str
    summary: str
    report: str