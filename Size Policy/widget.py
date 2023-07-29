from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy, QPushButton, QLineEdit
class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size Policy and Stretches")

        label = QLabel("Some text :")
        line_edit = QLineEdit()

        # Horizontal, Vertical
        # line_edit.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)  # default
        # see how weird  it is
        line_edit.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button1,3)
        h_layout_2.addWidget(button2,2)
        h_layout_2.addWidget(button3,1)
        # Stretch the widget to see the effect

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)
