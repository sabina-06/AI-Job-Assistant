import pandas as pd


def calculate_ats_score(found_skills):

    skills_df = pd.read_csv("data/skills.csv")

    total_skills = len(skills_df)

    score = (len(found_skills) / total_skills) * 100

    return round(score, 2)
