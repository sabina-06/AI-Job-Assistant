def generate_suggestions(missing_skills):

    suggestions = []

    if "Docker" in missing_skills:
        suggestions.append(
            "Learn Docker and mention any containerization projects."
        )

    if "AWS" in missing_skills:
        suggestions.append(
            "Adding AWS or any cloud experience will strengthen your resume."
        )

    if "FastAPI" in missing_skills:
        suggestions.append(
            "Build a REST API project using FastAPI."
        )

    if "Git" in missing_skills:
        suggestions.append(
            "Show Git version control experience through GitHub projects."
        )

    if "Linux" in missing_skills:
        suggestions.append(
            "Mention Linux commands or deployment experience."
        )

    if not suggestions:

        suggestions.append(
            "Excellent! Your resume covers most required skills."
        )

    return suggestions
