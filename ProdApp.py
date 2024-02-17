from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

# Виджет Qt — окно.
window = QWidget()
window.show()  # Важно: окно по умолчанию скрыто.

# Запуска цикла событий.
app.exec()