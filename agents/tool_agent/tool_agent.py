#tool_agent.py
import time
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
        if "429" in str(e):
            print("Rate limit hit. Sleeping for 15 seconds...")
            time.sleep(15)
            #continue
                
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
time.sleep(15)
if model_reply.startswith("CALCULATE:"):
    expression = model_reply.replace("CALCULATE:","").strip()
    
    result = calculator(expression)
    
    final_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
    User asked:
    
    {question}
    
    Calculator result:
    
    {result}
    
    Provide a helpful final answer.
    """
    )
    
    print("\nFinal Answer:")
    print(final_response.text)
    
#    print("\nTool Used: Calculator")
#    print("Expression:", expression)
#    print("Result:", result)



else:
    print("\nDirect Answer:")
    print(model_reply)