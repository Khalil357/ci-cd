from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Times", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# Create instance of FPDF class
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Set font to Times New Roman, size 12
pdf.set_font("Times", size=12)

# Read the file
with open('CI_CD_Assessment.md', 'r', encoding='utf-8') as file:
    text = file.read()

# Split into paragraphs to add spacing between them
paragraphs = text.split('\n\n')

for p in paragraphs:
    if p.strip() == '':
        continue
    # multi_cell params: w (width, 0=100%), h (line height), text
    # 1.5 line spacing for size 12 (12pt ~ 4.2mm) -> 4.2 * 1.5 = 6.3mm. Let's use 6.5.
    pdf.multi_cell(0, 6.5, p.replace('\n', ' '))
    # Add an empty line after paragraph
    pdf.ln(6.5)

pdf.output("CI_CD_Assessment.pdf")
print("PDF created successfully!")
