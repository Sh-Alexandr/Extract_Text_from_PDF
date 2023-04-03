# pip install pypdf2

import PyPDF2
pdf = open("test.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)
print(reader)
page = reader.pages[0]
print(page.extract_text())