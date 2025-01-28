from flask import Flask, request, jsonify
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

app = Flask(__name__)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local("vector_store", embeddings)

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vector_store.as_retriever()
)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = qa_chain.run(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)