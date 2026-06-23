#summary_agent.py
import time
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


print("current working directory:", os.getcwd())

from google import genai
from dotenv import load_dotenv
#import os

project_root = os.path.dirname(
     os.path.dirname(os.path.abspath(__file__))
)

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Load extracted paper text 
#with open ("C:\Users\Shridhar_Shukla_AI\OneDrive\Documents\2026\5-Day AI Agents-google\Capstone project\AI-Research-Assistant-Agent\docs/extracted_text.txt", 
#with open ("..\..\docs/extracted_text.txt", 
with open ("docs/extracted_text.txt", 
                    "r",
                    encoding="utf-8") as f:
   paper_text = f.read()
               

""" #You are a research paper analyst.
Read the paper and generate:

1. Executive Summary
2. key Idea
3. Main Contributions
"""

prompt = f"""
You are an expert AI research assistant.

Analyze the following research paper and provide:

1. Executive Summary (5 bullet points)
2. Main Idea
3. Why this paper was important
3. Key Contributions

Paper:

{paper_text[:15000]}
"""

#lets improve the agent now rather than later
#Wrap the API call below -
# step 1 : at the top - import time, step 2- wrap the API section below -
# ------ previos -----
""" response = client.models.generate_content(
      model="gemini-2.5-flash",
      contents=prompt
)   """
# ---- wraped above as below code ------
# this improved API call waits for 10 seconds and retries again everytime if it gets busy , istead of giving errors directly.
max_retries = 3

for attempt in range(max_retries):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
       
        print("Gemini call successfull")
        break
       
    except Exception as e:
         print(f"Attempt {attempt + 1} failed")
         print(e)
         
         if attempt < max_retries - 1:
             print("waiting 10 seconds before retry...")
             time.sleep(10)
         else:
             raise
             
 # ------- API wrap end -------
 
print(response.text)

# save outputs 
#with open("../../docs/summary_report.txt",
# updte 2 : save outputs
"""
with open("docs/summary_report.txt",
           "w",
           encoding="utf-8") as f:
       f.write(response.text)
       
print("\nSummary saved to docs/summary_report.txt")  """

# repllce above save code with below
"""
output_path = os.path.join(
    project_root,
    "docs",
    "summary_report.txt"
 )
"""

docs_folder = os.path.join(project_root, "docs")

os.makedirs(docs_folder, exist_ok=True)

output_path = os.path.join(
    docs_folder,
    "summary_report.txt"
 )

with open(output_path, "w", encoding="utf-8") as f:
    f.write(response.text)
      
print(f"Summary saved to: {output_path}")
