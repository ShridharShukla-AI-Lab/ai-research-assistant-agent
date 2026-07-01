import fitz
#pdf_path = "../sample_papers/paper.pdf"   #now the coordinator will pass the path 
import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

#the below path is printing inside agents section but not in docs folder of root directory hence use only BASE_DIR 
"""
project_root = os.path.dirname(
     os.path.dirname(os.path.abspath(__file__))
)
"""

def extract_pdf_text(pdf_path):
    
    doc = fitz.open(pdf_path)

    full_text = ""

    for page in doc:
        full_text += page.get_text()
        
#    print("Characters extracted:", len(full_text))
#    print("\nFirst 2000 characters:\n")
#    print(full_text[:2000])

    #with open("../docs/extracted_text.txt", "w", encoding="utf-8") as f:
    #    f.write(full_text)
    ## save to root docs folder with new approach os.path.join() 
    doc.close()
    
    
    docs_folder = os.path.join(BASE_DIR, "docs")    
    
    os.makedirs(docs_folder, exist_ok=True)
    
    output_path = os.path.join(
          docs_folder,
          "extracted_text.txt"
    )
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    
        
    return full_text
        
     
if __name__ == "__main__":
    paper_text = extract_pdf_text(pdf_path)
    print("PDF extracted successfully.")
    