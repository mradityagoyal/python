from subprocess import call

NUM_SLIDES = 17
COURSE_NAME = 'CSharp_'
#sleep interval
FIRST_SLIDE = 1

img_dir = 'resources/captures'
pdf_dir = 'resources/pdf'
for i in range(FIRST_SLIDE,FIRST_SLIDE+NUM_SLIDES):
    captureFile = "%s/%s%s.png" % (img_dir, COURSE_NAME, i)
    outputPdf = "%s/%s%s" % (pdf_dir, COURSE_NAME, i)
    call (['tesseract', captureFile, '-l', 'eng', outputPdf , 'pdf'])

