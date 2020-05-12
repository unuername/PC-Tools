
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        loadUi('mainwindow.ui', self)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
