"""
MIT License

Copyright (c) 2021 Edvin Alvarado

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

assert sys.version_info >= (3,10), "must be Pyton 3.10 or newer"

def main(arg: list[str]) -> None:
    match arg[1]:
        case "merge":
            merge()
        case "split":
            split()
        case "rotate":
            rotate()


def rotate() -> None:
    filename = input("File Name: ")
    rotation = int(input("How much to rotate in degrees: "))

    inputpdf = PdfFileReader(open(f"{filename}.pdf", "rb"))
    output = PdfFileWriter()

    for i in range(inputpdf.numPages):
        output.addPage(inputpdf.getPage(i).rotateClockwise(rotation))

    with open(f"{filename}_rotated.pdf", "wb") as outputStream:
        output.write(outputStream)

def split() -> None:
    filename = input("File Name: ")

    inputpdf = PdfFileReader(open(f"{filename}.pdf", "rb"))

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(f"{filename}_%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)

def merge() -> None:
    output = PdfFileWriter()

    while True:
        filename = input("File Name: ")
        if filename == "":
            break
        inputpdf = PdfFileReader(open(f"{filename}.pdf", "rb"))
        for i in range(inputpdf.numPages):
            output.addPage(inputpdf.getPage(i))

    name = input("Name for merged pdf: ")
    with open(f"{name}.pdf", "wb") as outputStream:
        output.write(outputStream)


main(sys.argv)
