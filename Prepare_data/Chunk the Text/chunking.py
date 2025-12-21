import json
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load your cleaned text
with open("../cleaning@@extrack/cleaned_policy.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2. Configure the Splitter
# Note: chunk_size is in characters here, which is safer for beginners
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
    separators=["\n\n", "\n", " ", ""]
)

# 3. Create the chunks
raw_chunks = splitter.split_text(text)

# 4. Attach Metadata
final_data = []
for i, chunk_text in enumerate(raw_chunks):
    chunk_entry = {
        "chunk_id": i,
        "content": chunk_text,
        "metadata": {
            "document": "Student_CODE-OF-CONDUCT-MDKMITL-2021-V3.pdf",
            "department": "Medicine",
            "policy_type": "Conduct",
            "chunk_index": i
        }
    }
    final_data.append(chunk_entry)

# 5. Save as JSON (Best format for the next step)
with open("processed_chunks.json", "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=4, ensure_ascii=False)

print(f"✅ Created {len(final_data)} chunks.")
print("Saved to 'processed_chunks.json'")