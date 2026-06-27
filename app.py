import streamlit as st
from utils.llm import analyze_resume, tailor_resume
from utils.llm import generate_cover_letter, generate_interview_questions
from utils.report import generate_report
from utils.charts import score_gauge
from utils.pdf_parser import extract_text
from utils.skills import extract_skills, compare_skills
from utils.ats import calculate_ats_score
from utils.jd_score import jd_score
from utils.suggestions import generate_suggestions

st.set_page_config(
    page_title="AI Job Assistant",
    page_icon="📄",
    layout="wide"
)
# ----------------------------
# Session State Initialization
# ----------------------------

if "review" not in st.session_state:
    st.session_state.review = ""

if "tailored_resume" not in st.session_state:
    st.session_state.tailored_resume = ""

if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""

if "interview_questions" not in st.session_state:
    st.session_state.interview_questions = ""
with st.sidebar:
    st.title("🚀 AI Job Assistant")

    st.markdown("---")

    st.write("### Features")

    st.success("✅ Resume Upload")
    st.success("✅ ATS Score")
    st.success("✅ JD Matching")
    st.success("✅ AI Resume Review")
    st.success("✅ AI Resume Tailoring")
    st.success("✅ AI Cover Letter")
    st.success("✅ AI Interview Questions")

    st.markdown("---")

    st.info("Built with Python + Streamlit + Gemini AI")
st.title("📄 AI Job Assistant")

st.write("Upload your resume in PDF format.")

uploaded_file = st.file_uploader(
    "Choose your Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract Resume
    resume_text = extract_text(uploaded_file)

    # Extract Skills
    skills = extract_skills(resume_text)

    # ATS Score
    score = calculate_ats_score(skills)

    # -----------------------------
    # Job Description
    # -----------------------------
    st.subheader("📋 Job Description")

    jd = st.text_area(
        "Paste the Job Description",
        height=200
    )

    # Default values
    matched = []
    missing = []
    match_score = 0

    if jd:

        matched, missing = compare_skills(
            skills,
            jd
        )

        match_score = jd_score(
            matched,
            missing
        )

    # -----------------------------
    # Dashboard
    # -----------------------------
    st.subheader("📊 Resume Analysis Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.plotly_chart(
        score_gauge(score,"ATS Score"),
        use_container_width=True
        )

    with col2:
        st.plotly_chart(
        score_gauge(
        match_score,
        "Job Match"
       ),
       use_container_width=True
)

    with col3:
        st.metric(
            "Skills Found",
            len(skills)
        )

    with col4:
        st.metric(
            "Missing Skills",
            len(missing)
        )

    # -----------------------------
    # Resume Text
    # -----------------------------
    st.subheader("📄 Extracted Resume")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )

    # -----------------------------
    # Skills
    # -----------------------------
    st.subheader("✅ Skills Detected")

    if skills:
        cols = st.columns(4)

        for i, skill in enumerate(skills):
            cols[i % 4].success(skill)
    else:
        st.warning("No skills found.")

    # -----------------------------
    # JD Analysis
    # -----------------------------
    if jd:

        st.subheader("🎯 Matching Skills")

        if matched:
            for skill in matched:
                st.success(skill)
        else:
            st.warning("No matching skills found.")

        st.subheader("❌ Missing Skills")

        if missing:
            for skill in missing:
                st.error(skill)
        else:
            st.success("Excellent! No missing skills.")

        st.subheader("💡 Resume Suggestions")

        suggestions = generate_suggestions(missing)

        for suggestion in suggestions:
            st.info(suggestion)

        st.divider()

        st.subheader("🤖 AI Resume Review")

        if st.button("Analyze with Gemini AI"):
            with st.spinner("Analyzing your resume..."):
                st.session_state.review = analyze_resume(
                resume_text,
                jd
            )

                with st.expander("🤖 AI Resume Review", expanded=True):
                    st.markdown(st.session_state.review)
                

            

        st.divider()

        st.subheader("✨ AI Resume Tailoring")

        if st.button("Generate Tailored Resume"):
            if not jd.strip():
                st.warning("Please paste a Job Description first.")

            else:
                with st.spinner("Tailoring Resume..."):
                    st.session_state.tailored_resume = tailor_resume(
                    resume_text,
                    jd
                )

                    with st.expander("✨ Tailored Resume", expanded=True):
                        st.markdown(st.session_state.tailored_resume)
        st.divider()

        st.subheader("✉ AI Cover Letter Generator")

        company = st.text_input("Company Name")

        role = st.text_input("Job Role")

        if st.button("Generate Cover Letter"):
            if company and role and jd:
                with st.spinner("Generating..."):
                    st.session_state.cover_letter = generate_cover_letter(
                    resume_text,
                    company,
                    role,
                    jd
                )

                    with st.expander("✉ AI Cover Letter", expanded=True):
                        st.markdown(st.session_state.cover_letter)

            else:
                st.warning("Please fill all fields.")

        st.divider()

        st.subheader("🎤 AI Interview Preparation")

        if st.button("Generate Interview Questions"):
            if not jd.strip():
                st.warning("Please paste a Job Description first.")

            else:
                with st.spinner("Preparing Interview Questions..."):
                    st.session_state.interview_questions = generate_interview_questions(
                    resume_text,
                    jd
                )

                    with st.expander("🎤 Interview Questions", expanded=True):
                        st.markdown(st.session_state.interview_questions)

        if (
    st.session_state.review
    or st.session_state.tailored_resume
    or st.session_state.cover_letter
    or st.session_state.interview_questions):
            generate_report(
            "Career_Report.pdf",
            score,
            match_score,
            st.session_state.review,
            st.session_state.tailored_resume,
            st.session_state.cover_letter,
            st.session_state.interview_questions
        )

            with open("Career_Report.pdf", "rb") as pdf:
                st.download_button(
                    label="📄 Download Career Report",
                    data=pdf,
                    file_name="Career_Report.pdf",
                    mime="application/pdf"
                )

        