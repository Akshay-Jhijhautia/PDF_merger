from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs = ["Nextjs.pdf", "Styling.pdf"]

for pdf in pdfs:
    merger.append(pdf)

with open("merged-pdf.pdf", "wb") as f:
    merger.write(f)

merger.close()
