from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict, total=False):
    research: str
    writing: str
    review: str

def manager(state: AgentState):
    return {}

def researcher(state: AgentState):
    return {"research": "research output"}

def writer(state: AgentState):
    return {"writing": "writer output"}

def reviewer(state: AgentState):
    return {"review": "reviewer output"}

graph = StateGraph(AgentState)

graph.add_node("Manager", manager)
graph.add_node("Researcher", researcher)
graph.add_node("Writer", writer)
graph.add_node("Reviewer", reviewer)

graph.add_edge(START, "Manager")
graph.add_edge("Manager", "Researcher")
graph.add_edge("Manager", "Writer")
graph.add_edge("Manager", "Reviewer")

graph.add_edge("Researcher", END)
graph.add_edge("Writer", END)
graph.add_edge("Reviewer", END)

app = graph.compile()

img_data = app.get_graph().draw_mermaid_png()


with open("06_Multi_Agent/labo2_manager_worker.png", "wb") as f: 
    f.write(img_data)

print("Diagramme Mermaid Labo 2 généré : labo2_manager_worker.png")

