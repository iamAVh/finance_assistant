import faiss
import pickle
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = SentenceTransformer('all-MiniLM-L6-v2')
INDEX_PATH = "vector.index"
DOCS_PATH = "docs.pkl"

def retrieve_relevant_docs(query, top_k=3):
    try:
        index = faiss.read_index(INDEX_PATH)
        with open(DOCS_PATH, "rb") as f:
            docs = pickle.load(f)
        query_vec = EMBEDDING_MODEL.encode([query])
        _, indices = index.search(query_vec, top_k)
        return [docs[i] for i in indices[0]]
    except Exception as e:
        return [f"Error retrieving documents: {str(e)}"]
