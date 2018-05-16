#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO, open


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


pdfFile = urlopen('http://pythonscraping.com'
                  '/pages/warandpeace/chapter1.pdf', timeout=10)
# pdfFile=open('../pages/warandpeace/chatper1.pdf', 'rb')
try:
    outputString = readPDF(pdfFile)
    print(outputString)
finally:
    pdfFile.close
