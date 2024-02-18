from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
import sys

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("Главное окно")

        self.button1 = QPushButton(self)
        self.button1.setText("Фото")
        self.button1.move(50, 50)
        self.button1.clicked.connect(self.open_photo_window)

        self.button2 = QPushButton(self)
        self.button2.setText("Веб-камера")
        self.button2.move(50, 100)
        self.button2.clicked.connect(self.open_web_window)

    def open_photo_window(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName", "","All Files (*);;JPEG Files (*.jpg)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.new_window = QMainWindow()
            label = QLabel()
            label.setPixmap(pixmap)
            self.new_window.setCentralWidget(label)
            self.new_window.setGeometry(500, 500, 300, 300)
            self.new_window.setWindowTitle("Изображение")
        #-------------------------------------------------
            self.new_window.show()
        
    def open_web_window(self):
        new_window = QMainWindow()
        new_window.setGeometry(500, 500, 300, 300)
        new_window.setWindowTitle("Веб-камера")
        new_window.show()

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())