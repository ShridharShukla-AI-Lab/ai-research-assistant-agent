#coordinator_agent.py
import os
from dotenv import load_dotenv
#import google.generativeai as genai   - older version / switch to newer version below
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello"
)

print(response.text)

