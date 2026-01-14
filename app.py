import streamlit as st
from rag.pdf_loader import load_pdfs
from rag.vectorstore import build_vectorstore
from graph.workflow import build_graph

st.title("AutoResearch AI")

topic = st.text_input("Enter Research Topic:")
uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if st.button("Run AutoResearch"):

    # Load PDFs
    paths = []
    for f in uploaded_files:
        path = f"temp_{f.name}"
        with open(path, "wb") as out:
            out.write(f.read())
        paths.append(path)

    docs = load_pdfs(paths)
    vectorstore = build_vectorstore(docs)

    # Run agents
    graph = build_graph()
    state = {"topic": topic, "vectorstore": vectorstore}
    result = graph.invoke(state)

    st.subheader("Research Notes")
    st.write(state.get("research_notes", ""))
