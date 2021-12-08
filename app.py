import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


from rotateWindow import Ui_rotateWindow 

class rotateWindow(QMainWindow, Ui_rotateWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = rotateWindow()
    win.show()
    sys.exit(app.exec())
