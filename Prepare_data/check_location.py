import os

# 1. We use "../" to go UP from 'chat bot' to the main folder
# 2. We use the EXACT name you found in your 'ls' command
file_path = "../data sample of medicine major policy/Student_CODE-OF-CONDUCT-MDKMITL-2021-V3.pdf"

if os.path.isfile(file_path):
    if file_path.lower().endswith('.pdf'):
        print("✅ Found it! This is the correct PDF.")
        
        # Now you can safely run your PDF reader code here
    else:
        print("❌ File found, but it's not a PDF.")
else:
    print("❓ Still not found.")
    print(f"I'm looking for: {os.path.abspath(file_path)}")