from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    ats_score,
    job_match,
    review,
    tailored_resume,
    cover_letter,
    interview_questions
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>AI Career Assistant Report</b>", styles["Title"])
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(f"<b>ATS Score:</b> {ats_score}%", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Job Match:</b> {job_match}%", styles["BodyText"])
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph("<b>Resume Review</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(review.replace("\n","<br/>"), styles["BodyText"])
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph("<b>Tailored Resume</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(tailored_resume.replace("\n","<br/>"), styles["BodyText"])
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph("<b>Cover Letter</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(cover_letter.replace("\n","<br/>"), styles["BodyText"])
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph("<b>Interview Questions</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(interview_questions.replace("\n","<br/>"), styles["BodyText"])
    )

    doc.build(story)