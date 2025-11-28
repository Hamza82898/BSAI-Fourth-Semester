from flask import Flask, render_template, request, jsonify
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

app = Flask(__name__)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
index = faiss.read_index("university.index")
mapping = pickle.load(open("university_map.pkl", "rb"))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data["query"]
    k = int(data.get("k", 5))

    query_vec = model.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(query_vec)
    scores, ids = index.search(query_vec, k)

    results = []
    for i, score in zip(ids[0], scores[0]):
        rec = mapping[i]
        results.append({
            "question": rec['question'],
            "answer": rec['answer'],
            "tags": rec['tags'],
            "score": float(score)
        })
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)