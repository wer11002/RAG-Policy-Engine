import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA

load_dotenv()

# 1. Local Embeddings (Fast & Free on your MacBook Air)
# Note: You MUST re-run your PDF ingestion with this model!
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Load the Vector Database
db_path = "../Embeddings/chromaDB/my_vector_db"
vector_db = Chroma(persist_directory=db_path, embedding_function=embeddings)

# 3. Use Llama 3 via Groq
# 'llama-3.3-70b-versatile' is one of the most powerful models available on Groq
llm = ChatGroq(
    temperature=0, 
    model_name="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# 4. Build the RAG Pipeline
retriever = vector_db.as_retriever(search_kwargs={"k": 3})
rag_pipeline = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

# 5. Ask the question
print("--- Searching with Llama 3 (Groq) ---")
try:
    query = "how many topic can we focus on?"
    response = rag_pipeline.invoke(query)
    print("\n[ANSWER]:\n", response["result"])
except Exception as e:
    print(f"❌ Error: {e}")