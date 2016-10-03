from PyPDF2 import PdfFileMerger, PdfFileReader

merger = PdfFileMerger()
for num in range(1, 555):
    print num
    merger.append(PdfFileReader(file("%d.pdf" %num, 'rb')))

merger.write("Reframing_Photography.pdf")
