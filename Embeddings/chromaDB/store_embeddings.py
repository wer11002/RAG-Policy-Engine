import json
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# 1. Load the chunks
with open("../../Prepare_data/Chunk the Text/processed_chunks.json", "r", encoding="utf-8") as f:
    chunks_data = json.load(f)

# 2. Setup the "Multilingual" Embedding Model (Same as Search Script)
# This model is great for both Thai and English
embeddings = HuggingFaceEmbeddings(model_name="paraphrase-multilingual-MiniLM-L12-v2")

# 3. Convert your JSON data into LangChain "Documents"
docs = []
for item in chunks_data:
    new_doc = Document(
        page_content=item["content"],
        metadata=item["metadata"]
    )
    docs.append(new_doc)

# 4. Create the Vector Database using LangChain's Chroma
db_path = "./my_vector_db"
print("--- Creating Database (This may take a minute) ---")

vector_db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=db_path
)

print(f"✅ Successfully created LangChain-compatible DB with {len(docs)} chunks!")