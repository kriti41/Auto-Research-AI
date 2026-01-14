from langgraph.graph import StateGraph, END
from agents.planner import planner_agent
from agents.researcher import researcher_agent

def build_graph():
    graph = StateGraph(dict)
    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", researcher_agent)
    graph.set_entry_point("planner")
    graph.add_edge("planner", "researcher")
    return graph.compile()
