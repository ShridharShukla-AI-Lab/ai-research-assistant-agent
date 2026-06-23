from dotenv import load_dotenv
import os

load_dotenv(".env")

print("Current folder:", os.getcwd())
print("API key:", os.getenv("GOOGLE_API_KEY"))