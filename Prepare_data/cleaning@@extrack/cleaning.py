import re
import os
from PyPDF2 import PdfReader

# 1. Setup paths
file_path = "../../data sample of medicine major policy/Student_CODE-OF-CONDUCT-MDKMITL-2021-V3.pdf"
output_path = "cleaned_policy.txt"

def clean_text(raw_text):
    # Remove "Page X" or "Page 1 of 10" (case insensitive)
    text = re.sub(r'(?i)page\s*\d+(\s*of\s*\d+)?', '', raw_text)
    
    # Normalize spacing: Replace multiple spaces with a single space
    text = re.sub(r' +', ' ', text)
    
    # Fix Newlines: Replace 3 or more newlines with just 2 (keeps paragraphs separate)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Remove leading/trailing whitespace from each line
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    
    return text.strip()

# 2. Execution logic
try:
    reader = PdfReader(file_path)
    full_text = ""
    
    for page in reader.pages:
        content = page.extract_text()
        if content:
            full_text += content + "\n"

    if not full_text.strip():
        print("❌ Could not detect text. The file might be a scan.")
    else:
        # 3. Clean the text
        cleaned_text = clean_text(full_text)
        
        # 4. Save to file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)
            
        print(f"✅ Success! Cleaned file saved as: {output_path}")
        print(f"Original length: {len(full_text)} characters")
        print(f"Cleaned length: {len(cleaned_text)} characters")

except FileNotFoundError:
    print(f"❓ Path error: {os.path.abspath(file_path)}")