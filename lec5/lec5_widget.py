from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Main Window")

        button = QPushButton("Click")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def button_clicked(self):
        print("Button Clicked")

    def button_pressed(self):
        print("Button Pressed")

    def button_released(self):
        print("Button Released")
