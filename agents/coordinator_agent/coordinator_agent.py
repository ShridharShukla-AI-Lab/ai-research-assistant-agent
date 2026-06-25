#coordinator_agent.py

import os
from dotenv import load_dotenv
#import google.generativeai as genai   - older version / switch to newer version below
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def choose_agent(user_query):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        You are a router .
        
        Choose exactly one:
        
        TOOL
        RESEARCH
        
        Question: {user_query}
        
        """
    )

    return response.text.strip()


user_input = input("Ask something: ")
#agent_choice = choose_agent(user_input)
#print("Chosen Agent:", agent_choice)

agent_choice = choose_agent(user_input)
print("Chosen Agent:", agent_choice)
#####

# coordinator agent manages calling research agent and tool agent
# #create coordinator logic

from agents.research_agent.research_agent import research_topic
from agents.tool_agent.tool_agent import ask_tool_agent

#question = input("Ask something: ")
#above question is shifted to top to implement agent choice logic

# question variable is now replaced with user_input
#if any(word in question.lower() for word in ["calculate", "multiply", "divide", "+", "-", "*", "/"]):
#    result = ask_tool_agent(question)
if any(word in user_input.lower() for word in ["calculate", "multiply", "divide", "+", "-", "*", "/"]):
    result = ask_tool_agent(user_input)
    
else:
    result = research_topic(user_input)
    
    
print("\nFinal Answer:\n")
print(result)