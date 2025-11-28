import pandas as pd
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer

def clean(t):
    return " ".join(str(t).split())

df = pd.read_csv("university_qa.csv")
df['question_clean'] = df['question'].apply(clean)
df['answer_clean'] = df['answer'].apply(clean)
df['embed_text'] = df['question_clean']

print("Generating embeddings...")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

print("Encoding")
embeddings = model.encode(
    df['embed_text'].tolist(),
    show_progress_bar=True,
    convert_to_numpy=True,
)

faiss_index = faiss.normalize_L2(embeddings)

d = embeddings.shape[1]
index = faiss.IndexFlatIP(d)
index.add(embeddings)

faiss.write_index(index, "university.index")
print("FAISS index Saved")

mapping = df.to_dict(orient='records')
pickle.dump(mapping, open("university_map.pkl", "wb"))
print("Mapping Saved")
