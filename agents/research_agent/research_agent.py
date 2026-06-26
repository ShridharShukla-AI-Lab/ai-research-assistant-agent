#research_agent.py
#development step4: before coordinator_agent and other agents can use this agent, we need to convert it from: standalone script ->to-> reusable function ->to-> callable agent. (this is the first real software-engineering refactor of the project.  
import os
from dotenv import load_dotenv
from google import genai

#load environment
load_dotenv()

#initialize API key
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
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
"""
response = client.models.generate_content(
       model="gemini-2.5-flash",
       contents=prompt
)
"""

##step 4: convert above 'response' to callable function :
# Gemini call

def research_topic(topic):
    response = client.models.generate_content(
           model="gemini-2.5-flash",
           contents=f"Research and explain: {topic}"
    )
    
    return response.text
    

if __name__ == "__main__":
    
    topic = input("Enter topic: ")
    
    result = research_topic(topic)
    
    print(result)
    # xxxxxxx callable function end xxxxxxxx
    # important: with( __name__ = __main__ ) , now if we run this agent directly, it behaves exactly as before but now other python can import and call it.


    # Save output
    output_path = os.path.join(
          "docs",
          "research_answer.txt"
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)
    #    f.write(response.text)
       

    print("Research answer saved.")