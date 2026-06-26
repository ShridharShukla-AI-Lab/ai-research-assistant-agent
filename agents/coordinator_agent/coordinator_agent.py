#coordinator_agent.py

import os
from dotenv import load_dotenv
#import google.generativeai as genai   - older version / switch to newer version below
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def choose_agent(user_query):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        You are a router .
        
        Choose exactly one:
        
        TOOL
        RESEARCH
        SUMMARY
        CONTRIBUTIONS
        LIMITATIONS
        
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

# coordinator agent manages calling RESEARCH agent, TOOL agent, SUMMARY agent, CONTRIBUTIONS agent and LIMITATIONS agent.
# #create coordinator logic

from agents.research_agent.research_agent import research_topic
from agents.tool_agent.tool_agent import ask_tool_agent

from agents.summary_agent.summary_agent import summarize_paper
from agents.contribution_agent.contribution_agent import extract_contributions
from agents.limitation_agent.limitation_agent import analyze_limitations

#question = input("Ask something: ")
#above question is shifted to top to implement agent choice logic

# question variable is now replaced with user_input
#if any(word in question.lower() for word in ["calculate", "multiply", "divide", "+", "-", "*", "/"]):
#    result = ask_tool_agent(question)

"""
if any(word in user_input.lower() for word in ["calculate", "multiply", "divide", "+", "-", "*", "/"]):
    result = ask_tool_agent(user_input)
    
else:
    result = research_topic(user_input)
 """
# #since gemini already returns agent_choice(i.e agent_choice = choose_agent())
# #hence above keyword logic not required anymore.
# replacing the entire block with below :
if agent_choice == "TOOL":
    result = ask_tool_agent(user_input)
    
elif agent_choice == "RESEARCH":
    result = research_topic(user_input)
  
elif agent_choice == "SUMMARY":
    result = summarize_paper()
    
elif agent_choice == "CONTRIBUTIONS":
    result = extract_contributions()
    
elif agent_choice == "LIMITATIONS":
    result = analyze_limitations()
    
    
else:
    result = "No suitable agent found."
    
print("\nFinal Answer:\n")
print(result)

"""    
elif agent_choice == "SUMMARY":
    result = summarize_paper(user_input)
    
elif agent_choice == "CONTRIBUTIONS":
    result = extract_contributions(user_input)
    
elif agent_choice == "LIMITATIONS":
    result = analyze_limitations(user_input)    #above will be refactored in next logic update
"""