from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication   
import sys

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("Главное окно")

        self.button1 = QPushButton(self)
        self.button1.setText("Фото")
        self.button1.move(50, 50)

        self.button2 = QPushButton(self)
        self.button2.setText("Веб-камера")
        self.button2.move(50, 100)

        self.button3 = QPushButton(self)
        self.button3.setText("Видео")
        self.button3.move(50, 150)

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())