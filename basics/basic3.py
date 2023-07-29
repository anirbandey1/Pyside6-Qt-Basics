# VERSION 3 : Setting up a separate class
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Push me")
        # Set our button as the central widget
        self.setCentralWidget(button)





app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
