from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

def planner_agent(state):
    topic = state["topic"]
    plan = llm.predict(f"Create a research plan for topic: {topic}")
    state["plan"] = plan
    return state
