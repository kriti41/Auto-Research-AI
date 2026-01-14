from langchain.document_loaders import PyMuPDFLoader

def load_pdfs(paths):
    docs = []
    for path in paths:
        loader = PyMuPDFLoader(path)
        docs.extend(loader.load())
    return docs
