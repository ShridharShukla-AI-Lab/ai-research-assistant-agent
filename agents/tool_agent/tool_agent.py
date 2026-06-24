#tool_agent.py
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


#Tool
def calculator(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"
        
     
question = input("Ask a question: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
You are an assistant.

If the user asks a mathematical calculation, reply 
 ONLY in this format:
 
CALCULATE: expression

Examples:
CALCULATE: 25*4
CALCULATE: (100+50)/3

otherwise answer normally.

User Question:
{question}
"""
)

model_reply = response.text.strip()

#print("\nModel Reply:")
#print(model_reply)

if model_reply.startswith("CALCULATE:"):
    expression = model_reply.replace("CALCULATE:","").strip()
    
    result = calculator(expression)
    
    print("\nTool Used: Calculator")
    print("Expression:", expression)
    print("Result:", result)
else:
    print("\nDirect Answer:")
    print(model_reply)