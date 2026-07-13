# -*- coding: utf-8 -*-
import os, fitz
import win32com.client as win32

DOCX = r"C:\Users\hiond\class\srs\output\솔루션요구사항정의서.docx"
OUT  = r"C:\Users\hiond\AppData\Local\Temp\claude\C--Users-hiond-class-srs\ce7a4926-6f12-4d6a-a52e-885fc1bde5ce\scratchpad"
PDF  = os.path.join(OUT, "srs_final.pdf")

word = win32.Dispatch("Word.Application"); word.Visible = False
try:
    d = word.Documents.Open(DOCX)
    d.SaveAs(PDF, FileFormat=17)  # wdFormatPDF
    d.Close(False)
finally:
    word.Quit()

print("PDF exists:", os.path.exists(PDF), "size:", os.path.getsize(PDF) if os.path.exists(PDF) else 0)
doc = fitz.open(PDF)
print("pages:", doc.page_count)
for i in range(doc.page_count):
    pix = doc[i].get_pixmap(dpi=110)
    pix.save(os.path.join(OUT, f"srs_page_{i+1:02d}.png"))
print("rendered:", doc.page_count)
