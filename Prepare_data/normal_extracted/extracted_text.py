from PyPDF2 import PdfReader

# File path
file_path = "../data sample of medicine major policy/Student_CODE-OF-CONDUCT-MDKMITL-2021-V3.pdf"
try:
    reader = PdfReader(file_path)
    text_list = [] # We store pages in a list first
    

    for page in reader.pages:
        content = page.extract_text()
        if content and content.strip(): # Check if it's not just empty spaces
            text_list.append(content)
    
    # Check if we actually found any text
    if not text_list:
        print("Error: Could not detect any text. The PDF might be an image/scan.")
    else:
        # Join the list into one big string
        final_text = "\n".join(text_list)
        print(f"Success! Character count: {len(final_text)}")
        
        # --- NEW: SAVE TO A .TXT FILE ---
        with open("extracted_policy.txt", "w", encoding="utf-8") as f:
            f.write(final_text)
        print("The text has been saved to 'extracted_policy.txt'")

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
except Exception as e:
    print(f"Something went wrong: {e}")