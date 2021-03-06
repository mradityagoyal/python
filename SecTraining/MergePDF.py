from PyPDF2 import PdfFileMerger






NUM_SLIDES = 17
COURSE_NAME = 'CSharp_'
#sleep interval
FIRST_SLIDE = 1

pdf_dir = 'resources/pdf'
pdfs = ["%s/%s%s.pdf" % (pdf_dir, COURSE_NAME, i) for i in range(FIRST_SLIDE, FIRST_SLIDE+NUM_SLIDES)]
# pdfs = ["%s/%s%s.pdf" % (pdf_dir, COURSE_NAME, i) for i in range(1,3)]
merger = PdfFileMerger()
for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('resources/backup/CSharp_.pdf', 'wb') as fout:
    merger.write(fout)

