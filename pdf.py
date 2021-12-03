# pdf utilities for some common tasks that are currently not implemented (well) in adobe reader or PDF24

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
