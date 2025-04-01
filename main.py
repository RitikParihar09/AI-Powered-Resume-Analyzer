from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import PyPDF2 as pdf  
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract text from PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):  
        text += reader.pages[page].extract_text() or ""  
    return text

# Function for AI response
def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content, prompt])
    return response.text

# Streamlit UI Setup
st.set_page_config(page_title="Resume Analyzer")
st.header("AI-Powered Resume Analyzer")

input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF Only)", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ PDF Successfully uploaded!")

# Prompt Definitions
prompts = {
    "resume_summary": """
    Provide a detailed summary of the resume, highlighting key qualifications, experiences, and notable achievements.
    """,
    "percentage_match": """
    Compare the resume with the job description and provide a percentage match score.
    Explain how well the resume fits the job role based on skills, experience, and keywords.
    """,
    "skill_improvement": """
    Analyze the resume against the provided job description. Identify relevant technical and soft skills.  
    For each skill in the job description:  
    - If the skill is present in the resume, mark it as ✅.  
    - If the skill is missing, mark it as ❌.  
    Provide a structured table format for easy readability.  
    """,
    "missing_keywords": """
    Extract key skills from the job description and compare them with the resume.
    Identify missing or weak keywords that could improve ATS optimization.
    """,
    "interview_prep": """
    Based on the resume and job description, generate a list of potential interview questions.
    Include both technical and behavioral questions.
    """,
    "personalized_recommendations": """
    Based on the resume and job description, provide personalized recommendations for improving the resume. Suggest relevant courses, certifications, and projects that could enhance the candidate's profile.
    """,
    "role_fitment_score": """
    Provide a percentage score (out of 100) on how well the resume aligns with the job description. Consider the match between the skills, experience, and qualifications required for the role.
    """,
    "skill_proficiency": """
    Based on the resume and job description, evaluate the proficiency level of each skill (basic, intermediate, advanced). Provide feedback on how the candidate can improve their proficiency in each skill.
    """
}

# Button Actions
if st.button("Summarize my Resume"):
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, prompts["resume_summary"])
        st.subheader("Resume Summary:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume.")

if st.button("Percentage Match"):
    if uploaded_file is not None and input_text:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, prompts["percentage_match"])
        st.subheader("Job Match Percentage:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume and provide a job description.")

if st.button("How can I improve my skills?"):
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, prompts["skill_improvement"])
        st.subheader("Skill Improvement Suggestions:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume.")

if st.button("Find Missing Keywords"):
    if uploaded_file is not None and input_text:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, prompts["missing_keywords"])
        st.subheader("Missing Keywords for ATS Optimization:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume and provide a job description.")

if st.button("Interview Preparation"):
    if uploaded_file is not None and input_text:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, prompts["interview_prep"])
        st.subheader("Interview Questions Based on Your Resume:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume and provide a job description.")

if st.button("Personalized Recommendations"):
    if uploaded_file is not None and input_text:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, prompts["personalized_recommendations"])
        st.subheader("Personalized Recommendations:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume and provide a job description.")

if st.button("Job Role Fitment Score"):
    if uploaded_file is not None and input_text:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, prompts["role_fitment_score"])
        st.subheader("Job Role Fitment Score:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume and provide a job description.")

if st.button("Skill Proficiency Levels"):
    if uploaded_file is not None and input_text:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, prompts["skill_proficiency"])
        st.subheader("Skill Proficiency Levels:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume and provide a job description.")
