from PySide6.QtWidgets import QMainWindow, QPushButton

# Building on top of QMainWindow
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press me")
        self.setCentralWidget(button)

