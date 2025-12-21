import json
import chromadb
from chromadb.utils import embedding_functions

# 1. Load the chunks we created in the last step
with open("../../Prepare_data/Chunk the Text/processed_chunks.json", "r", encoding="utf-8") as f:
    chunks_data = json.load(f)

# 2. Initialize ChromaDB (it will create a folder named 'my_vector_db')
client = chromadb.PersistentClient(path="./my_vector_db")

# 3. Choose an Embedding Model (Free/Local)
# This model converts Thai/English text into 384-dimensional vectors
emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

# 4. Create a "Collection" (Like a table in a database)
collection = client.get_or_create_collection(
    name="medicine_policies", 
    embedding_function=emb_fn
)

# 5. Prepare data for the database
ids = []
documents = []
metadatas = []

for item in chunks_data:
    ids.append(str(item["chunk_id"]))
    documents.append(item["content"])
    metadatas.append(item["metadata"])

# 6. Add to the database
collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print(f"✅ Successfully embedded {len(documents)} chunks into ChromaDB!")