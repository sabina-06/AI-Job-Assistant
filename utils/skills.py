import pandas as pd

# Read the skills database
skills_df = pd.read_csv("data/skills.csv")

# Convert skill column into a list
skill_list = skills_df["skill"].tolist()


def extract_skills(text):
    """
    Extract matching skills from resume text.
    """
    found_skills = []

    text = text.lower()

    for skill in skill_list:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


def compare_skills(resume_skills, jd_text):
    """
    Compare resume skills with job description.
    Returns matched and missing skills.
    """

    jd_text = jd_text.lower()

    matched = []
    missing = []

    for skill in resume_skills:
        if skill.lower() in jd_text:
            matched.append(skill)

    for skill in skill_list:
        if skill.lower() in jd_text and skill not in resume_skills:
            missing.append(skill)

    return matched, missing
