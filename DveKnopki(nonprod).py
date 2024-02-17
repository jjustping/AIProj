import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Главное меню")
        self.setMinimumSize(QSize(600, 400))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()