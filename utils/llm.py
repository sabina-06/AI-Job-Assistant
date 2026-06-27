import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


# ==========================================================
# AI Resume Review
# ==========================================================

def analyze_resume(resume_text, jd):
    """
    Analyze the resume against the given Job Description.
    """

    prompt = f"""
You are an expert ATS reviewer and Senior Software Engineering Recruiter.

Analyze the following resume against the given Job Description.

Return the response in Markdown using ONLY these headings.

# Overall ATS Evaluation

Give an ATS score out of 100.
Explain why.

# Resume Summary

Write a concise 3-4 line summary.

# Strengths

Provide bullet points.

# Weaknesses

Provide bullet points.

# Missing Skills

Mention important missing skills required for this job.

# Resume Improvements

Give practical suggestions to improve the resume.

# Interview Questions

Generate 8 interview questions based on the resume.

Resume:
{resume_text}

Job Description:
{jd}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error while analyzing resume:\n\n{str(e)}"


# ==========================================================
# AI Resume Tailoring
# ==========================================================

def tailor_resume(resume_text, jd):
    """
    Tailor the resume according to the Job Description.
    """

    prompt = f"""
You are an experienced technical recruiter.

Rewrite the following resume specifically for this Job Description.

Return the answer in Markdown using ONLY these headings.

# Professional Summary

Rewrite the summary.

# Improved Project Descriptions

Rewrite project descriptions using stronger action verbs
and measurable achievements.

# Keywords to Add

List ATS keywords that should be added.

# Resume Tips

Provide five practical suggestions.

Resume:
{resume_text}

Job Description:
{jd}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error while tailoring resume:\n\n{str(e)}"


# ==========================================================
# AI Cover Letter Generator
# ==========================================================

def generate_cover_letter(resume_text, company, role, jd):
    """
    Generate a professional cover letter.
    """

    prompt = f"""
You are an expert technical recruiter.

Write a professional cover letter.

Candidate Resume:
{resume_text}

Company:
{company}

Role:
{role}

Job Description:
{jd}

Requirements:

- Professional business tone
- Around 300-400 words
- Mention relevant technical skills
- Mention important projects
- Explain why the candidate is a strong fit
- End with a professional closing
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error while generating cover letter:\n\n{str(e)}"


# ==========================================================
# AI Interview Question Generator
# ==========================================================

def generate_interview_questions(resume_text, jd):
    """
    Generate interview questions based on the resume
    and Job Description.
    """

    prompt = f"""
You are a Senior Software Engineering Interviewer.

Based on the resume and Job Description, generate interview preparation material.

Return ONLY these sections in Markdown.

# Technical Questions

Generate 10 technical interview questions.

# Coding Topics to Revise

Suggest important DSA topics.

# Project Questions

Generate project-specific questions.

# HR Questions

Generate five HR interview questions.

# Preparation Tips

Provide practical preparation advice.

Resume:
{resume_text}

Job Description:
{jd}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error while generating interview questions:\n\n{str(e)}"