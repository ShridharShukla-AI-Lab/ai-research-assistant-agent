import fitz
pdf_path = "../sample_papers/paper.pdf"

doc = fitz.open(pdf_path)

full_text = ""

for page in doc:
    full_text += page.get_text()
    
print("Characters extracted:", len(full_text))

print("\nFirst 2000 characters:\n")
print(full_text[:2000])


with open("../docs/extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(full_text)
                           