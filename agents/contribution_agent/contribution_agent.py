#contribution_agent subset from summary_agent
#development step4: before coordinator_agent and other agents can use this agent, we need to convert it from: standalone script ->to-> reusable function ->to-> callable agent. (this is the first real software-engineering refactor of the project.
#next step: make summary agent callable - to implement multi agent collaboration. this demonstrates agent collaboration, which is valuable for interviews and GitHub.
import time
import os
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#the above path is printing inside agents section but not in docs folder of root directory
#apply changes below
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

print("current working directory:", os.getcwd())

from google import genai
from dotenv import load_dotenv
#import os

#the below path is printing inside agents section but not in docs folder of root directory hence use only BASE_DIR 
"""
project_root = os.path.dirname(
     os.path.dirname(os.path.abspath(__file__))
)
"""
# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Load extracted paper text 
#with open ("C:\Users\Shridhar_Shukla_AI\OneDrive\Documents\2026\5-Day AI Agents-google\Capstone project\AI-Research-Assistant-Agent\docs/extracted_text.txt", 
#with open ("..\..\docs/extracted_text.txt", 

def extract_contributions(paper_text=None):
    
    if paper_text is None:
        
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

    ## in contribution agent change prompt and fubction from how it was in summary agent.
    #def summarize_paper(paper_text):

#def extract_contributions(paper_text):

    prompt = f"""
    You are an expert AI research analyst.

    Analyze the following research paper.
    
    Identify ONLY the major contributions.
    
    For each contribution provide:

    1. Contribution title
    2. Explanation
    3. Why it is novel
    4. Practical impact
    
    Do NOT summarize the paper.
    
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
     
    #print(response.text)

    ##step 5: make summary agent callable function
    """  
    def summarize_text(text):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Summarize the following:\n\n{text}"
        )
        
        return response.text
      """  
    ##instead above function we are making entire (read, prompt. response, save) things logic as callable function.

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

    docs_folder = os.path.join(BASE_DIR, "docs")

    os.makedirs(docs_folder, exist_ok=True)

    output_path = os.path.join(
          BASE_DIR,
          "docs",
          "contribution_report.txt"
     )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)
          
    print(f"Contributions Summary saved to: {output_path}")
    
    
    
    return response.text
    
if __name__ == "__main__":
#    pdf_text = paper_text
#    print(extract_contributions(paper_text))
    print(extract_contributions())
    
