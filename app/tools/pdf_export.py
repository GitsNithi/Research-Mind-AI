from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(report):

    doc = SimpleDocTemplate("Research_Report.pdf")

    styles = getSampleStyleSheet()

    story = []

    for line in report.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))

    doc.build(story)

    return "Research_Report.pdf"