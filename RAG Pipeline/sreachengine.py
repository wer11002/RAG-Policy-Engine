import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

load_dotenv()  # load .env file

# 1. Setup the Brain (Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Safety check (optional but recommended)
if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError("GOOGLE_API_KEY is missing")

# 2. Setup the "Librarian" (The Retriever)
retriever = vector_db.as_retriever()

# 3. Create the RAG Pipeline
rag_pipeline = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

# 4. Ask a question
response = rag_pipeline.invoke(
    "What is the policy for late assignment submission?"
)
print(response["result"])
