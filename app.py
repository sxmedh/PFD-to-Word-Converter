from pdf2docx import Converter, parse

pdf_file = 'sample.pdf'
word_file = 'sample.docx'

cv = Converter(pdf_file)
cv.convert(word_file, start=0, end=None)
cv.close()

parse(pdf_file, word_file, start=0, end=None)
