from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = FAISS.from_documents(documents, embeddings)

vector_store.save_local("vector_store")