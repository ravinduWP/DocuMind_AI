from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_embedding():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def build_vectorstore(chunks, embeddings):
    vectorstore = Chroma.from_texts(chunks, embeddings)
    return vectorstore

def search(vectorstore, query, k=3):
    results = vectorstore.similarity_search(query, k=k)
    return results
