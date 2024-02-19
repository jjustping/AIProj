import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
import cv2

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Webcam")

        # Кнопка для открытия окна с вебкамерой
        self.button_webcam = QPushButton("Open Webcam")
        self.button_webcam.clicked.connect(self.open_webcam)

        # Кнопка для открытия окна с фотографией
        self.button_photo = QPushButton("Open Photo")
        self.button_photo.clicked.connect(self.open_photo_window)

        # Вертикальный компоновщик и добавляем в него кнопки
        layout = QVBoxLayout()
        layout.addWidget(self.button_webcam)
        layout.addWidget(self.button_photo)

        # Главный виджет и устанавливленный в него компоновщик
        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)

    def open_webcam(self):
        # Новое окно с вебкамерой
        self.webcam_window = WebcamWindow()
        self.webcam_window.show()

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
            self.new_window.show()

class WebcamWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Webcam")

        self.label = QLabel(self)
        self.setCentralWidget(self.label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        self.video_capture = cv2.VideoCapture(0)

    def update_frame(self):
        ret, frame = self.video_capture.read()

        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            pixmap = QPixmap.fromImage(QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888))
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.AspectRatioMode.KeepAspectRatio))

    def closeEvent(self, event):
        self.timer.stop()
        self.video_capture.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec_())