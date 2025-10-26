from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
import os

pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))

base_dir = os.path.expanduser("~/codebase_genius")
os.makedirs(base_dir, exist_ok=True)

md_path = os.path.join(base_dir, "Codebase_Genius_Project_Report.md")
pdf_path = os.path.join(base_dir, "Codebase_Genius_Project_Report.pdf")

markdown_content = """# 🧠 Codebase Genius: AI-Powered Documentation Generator
**Author:** Evans Langat  
**Date:** October 2025  

---

## 1. Introduction
Codebase Genius is an AI-driven system that automatically generates comprehensive documentation for GitHub repositories.

## 2. Objective
- Automate documentation generation.  
- Improve maintainability and knowledge transfer.  
- Serve as foundation for Jaseci-based intelligent systems.

## 3. Workflow
1. Accept repository input and validate it.  
2. Map repository structure and analyze files.  
3. Prioritize main modules (main.py, app.py).  
4. Generate Markdown documentation.

## 4. Implementation
Modules:
- code_genius.py – core logic  
- __main__.py – supervisor interface  
- output/DOCUMENTATION.md – generated result  

## 5. Results
Generated documentation successfully for multiple Python files.  
Output saved in ~/codebase_genius/output/.

## 6. Challenges and Future Work
**Challenges**
- Parsing large repos.  
- Handling syntax errors.  

**Future Improvements**
- Add Jac graph walkers.  
- Generate relationship diagrams.  
- Build web/API interface.

## 7. Conclusion
Codebase Genius proves automated documentation is achievable and sets the stage for Jaseci-powered extensions.
"""

# Save Markdown version
with open(md_path, "w") as f:
    f.write(markdown_content)

# Create PDF
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="MyBodyText", fontName="HeiseiMin-W3", fontSize=11, leading=14))

doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
flow = []

for line in markdown_content.split("\n"):
    if line.startswith("# "):
        flow.append(Paragraph(f"<b><font size=16>{line[2:]}</font></b>", styles["MyBodyText"]))
    elif line.startswith("## "):
        flow.append(Spacer(1, 0.2 * inch))
        flow.append(Paragraph(f"<b><font size=13>{line[3:]}</font></b>", styles["MyBodyText"]))
    else:
        flow.append(Paragraph(line.replace("**", "").replace("`", ""), styles["MyBodyText"]))
    flow.append(Spacer(1, 0.15 * inch))

doc.build(flow)

print("✅ Report generated successfully!")
print("Markdown:", md_path)
print("PDF:", pdf_path)
