# app.py
import os
import streamlit as st
import base64
import streamlit.components.v1 as components
from PIL import Image
from agents.coordinator_agent.coordinator_agent import run_coordinator

# ------------ button design ----------------
#import streamlit as st

st.markdown("""
    <style>
    /* AI Modern Button Styling */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(270deg, #FF007A, #7928CA, #00C6FF, #1A73E8);
        background-size: 800% 800%;
        animation: AI-gradient 6s ease infinite;
        border: none;
        border-radius: 50px;
        color: white !important;
        font-weight: 800;
        font-size: 1.1rem;
        padding: 0.5rem 2rem;
        box-shadow: 0 4px 15px rgba(121, 40, 202, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 8px 25px rgba(0, 198, 255, 0.6);
        border: none;
    }

    @keyframes AI-gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .upload-card{
        padding:12px;
        border-radius:18px;
        border:1px solid #d8ebff;
        background:#f7fbff;
        box-shadow:0 8px 20px rgba(0,120,255,0.08);
        margin-top:5px;
        margin-bottom:10px;
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"]{
        background:#f8fbff;
        border-radius:18px;
        padding:12px;
    }
    
    </style>
""", unsafe_allow_html=True)




#    st.image("page_icon.png")
    
# This button will automatically inherit the beautiful design!

#col1, col2, col3 = st.columns([1, 2, 1])
#with col2:
#    st.button("❄️ SHRIDHAR SHUKLA - AI RESEARCH ASSISTANT 🥇", type="primary")

    
# -------------------------------------------
# Define app identifier for tracking
APP_URL = "https://shridhar-ai-research-assist.streamlit.app/"



st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🌐",
    layout="wide"
)


col1, col2 = st.columns([4, 1])
with col1:
    st.title("🌐 AI Research Assistant")
    st.button("⚡️️ SHRIDHAR SHUKLA - AI RESEARCH ASSISTANT 🥇 v1.0", type="primary")
    
with col2:
    #st.image("assets/page_icon.png", width=160)
    
    img = Image.open("assets/page_icon.png")
    img.putalpha(90)
    
    st.image(img, width=140)

#st.write("Welcome to the AI Research Assistant")

#st.divider()

#st.button("❄️ SHRIDHAR SHUKLA - AI RESEARCH ASSISTANT 🥇", type="primary")


st.markdown('<div class="upload-card">', unsafe_allow_html=True)       #begin soft glass card
#st.subheader("🚀Start Your Research Analysis")


with st.container(border=True):
    #st.markdown("### 📤 Upload a Research Paper (PDF)")
    uploaded_pdf = st.file_uploader(
        "📤 Upload a Research Paper (PDF)",
        type=["pdf"],
        help="Supported format: PDF"
    )

    research_query = st.text_input(
        "Or enter a research topic",
        placeholder="Example: Transformers in NLP, LLMs for healthcare, or upload a PDF."
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        analyze = st.button("❄️ Analyze", type="primary")


st.markdown("</div>", unsafe_allow_html=True)  #close the glass card


if analyze:
    if uploaded_pdf:
        
        os.makedirs("sample_papers", exist_ok=True)
        
        pdf_path = os.path.join(
            "sample_papers",
            uploaded_pdf.name
        )
        
        with open(pdf_path, "wb") as f:
            f.write(uploaded_pdf.getbuffer())
            
        #with st.spinner("🔍 Analyzing paper..."):
        status = st.status("🔍 Starting analysis...", expanded=True)
        status.write("💾 Saving uploaded PDF...")
        status.write("📃 Extracting text...")
        status.write("💡 Running AI analysis...")
        
        result = run_coordinator(f"Analyze {pdf_path}")
            
        #st.json(result)   - testing/view structure
        #st.success(f"PDF - {uploaded_pdf.name} saved successfully")
        status.update(
            label="✅️ Analysis completed successfully!",
            state="complete"
        )
        
        #st.write(pdf_path)
        #result = run_coordinator(f"Analyze  {pdf_path}")
        
        #make each sections collapsible by replacing .subheader with .expander -
        
        st.subheader("📜 Executive Summary")
        st.expander("📜 Executive Summary")
        st.write(result["summary"])
        
        st.divider()
        st.subheader("💡 Contributions")
        st.expander("💡 Contributions")
        st.write(result["contributions"])
        
        st.divider()
        st.subheader("⚠️ Limitations")
        st.expander("⚠️ Limitations")
        st.write(result["limitations"])
        
        
        #download report
        st.divider()
        st.subheader("📥Download")       
        st.download_button(
        #st.button(
            label="Download Analysis Report",
            data=f"""
        AI RESEARCH ASSISTANT REPORT
        ===============================================
        
        EXECUTIVE SUMMARY
        
        {result["summary"]}
        
        ===============================================
        
        KEY CONTRIBUTIONS
        
        {result["contributions"]}
        
        ===============================================
        
        LIMITATIONS
        
        {result["limitations"]}
        
        """,
            file_name="analysis_report.txt",
            mime="text/plain"
        )
        
        
        #Paper statistics
        st.divider()
        #paper_text = result   # since pdf extracted text file is read in 'result'.
        st.subheader("📊 Paper Statistics")
        
        summary = result["summary"]
        contributions = result["contributions"]
        limitations = result["limitations"]
        
        analysis_text = summary + contributions + limitations
        
        col1, col2, col3, col4 = st.columns(4)
        
        col1.metric("📝 Analysis words : ", len(analysis_text.split()))
        col2.metric("📜 Summary Words : ", len(summary.split()))
        col3.metric("💡 Key contributions : ", len(contributions.split(".")))
        pdf_size_mb = uploaded_pdf.size / (1024*1024)
        col4.metric("📰 PDF Size", f"{pdf_size_mb:.1f} MB")
        
        
        #sidebar
        with st.sidebar:
            st.title("Settings")
            """st.write("AI model")
            
            model = st.selectbox(
                "Choose Model",
                [
                     "gemini-2.5-flash",
                     "gemini-2.5-pro"
                ]
            )"""
            st.divider()
            st.subheader("🚀 Upcoming Features")
            st.write("👥💬 Chat with Paper")
            st.write("🗊🗐 Compare papers")
            st.write("📑 Citation Export")
            st.write("🔍 paper Search")
        
    elif research_query:
        
        with st.spinner("Researching..."):
            result = run_coordinator(research_query)
            
        st.write(result)
        #st.success(f"Research Topic: {research_query}")
        
    else:
        st.warning("Please upload a pdf or enter a research topic.")
        


# --- Footer with Visitor Count & Social ---
st.divider()
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; padding: 1rem 0; border-bottom: 1px solid #E8EAED; margin-bottom: 1rem;">
    <div style="display: flex; align-items: center; background-color: #F8F9FA; padding: 8px 16px; border-radius: 8px; border: 1px solid #DADCE0; color: #202124;">
        <span style="font-size: 18px; margin-right: 8px;">👁️</span>
        <img src="https://api.visitorbadge.io/api/visitors?path=shridhar-shukla-ai-dashboard&label=LIVE%20VISITORS&labelColor=%23ffffff&countColor=%231A73E8" alt="Live Visitor Count" style="height: 22px;">
    </div>
    <div style="margin-top: 10px;">
        <iframe src="https://www.facebook.com/plugins/like.php?href=https%3A%2F%2Fwww.facebook.com%2Fprofile.php%3Fid%3D61591182107658&width=150&layout=button_count&action=like&size=small&share=true&height=46" width="150" height="46" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true" allow="encrypted-media"></iframe>
    </div>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; color: #5F6368; font-size: 14px;">
    <p>&copy; 2026 AI Research Assistant. All rights reserved.</p>
    <div style="display: flex; gap: 24px;">
        <a href="#" style="color: #5F6368; text-decoration: none;">Privacy Policy</a>
        <a href="#" style="color: #5F6368; text-decoration: none;">Terms of Service</a>
        <a href="#" style="color: #5F6368; text-decoration: none;">Help Center</a>
    </div>
</div>
""", unsafe_allow_html=True)
