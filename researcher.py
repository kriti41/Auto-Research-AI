def researcher_agent(state):
    retriever = state["vectorstore"].as_retriever()
    docs = retriever.get_relevant_documents(state["topic"])
    state["research_notes"] = "\n".join([d.page_content for d in docs])
    return state
