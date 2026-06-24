#research_agent.py
import os
from dotenv import load_dotenv
from google import genai

#load environment
load_dotenv()

#initialize API key
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

#read extracted text from research paper
input_path = os.path.join(
     "docs",
     "extracted_text.txt"
)

with open(input_path, 'r', encoding="utf-8") as f:
    paper_text = f.read()
    

#research question(static)
question = """
What are the key contributions
of this research paper?
"""

#create prompt 
prompt = """
You are an expert AI researcher,

Research Paper:

(paper_text)

Question:

(question)

Provide a detailed answer,
Use bullet points.
"""

# Gemini call
response = client.models.generate_content(
       model="gemini-2.5-flash",
       contents=prompt
)

# Save output
output_path = os.path.join(
      "docs"
      "research_answer.txt"
)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(response.text)
    

print("Research answer saved.")