from langgraph.graph import StateGraph, START, END

from app.state.state import AgentState

from app.agents.planner import planner_agent
from app.agents.researcher import researcher_agent
from app.agents.reviewer import reviewer_agent
from app.agents.writer import writer_agent

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_agent)
workflow.add_node("researcher", researcher_agent)
workflow.add_node("reviewer", reviewer_agent)
workflow.add_node("writer", writer_agent)

workflow.add_edge(START, "planner")
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", "reviewer")
workflow.add_edge("reviewer", END)

app = workflow.compile()