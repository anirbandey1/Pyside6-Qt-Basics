from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout,QVBoxLayout, QPushButton

class Widget (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("../icons/minions.jpg"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)