from PySide6.QtWidgets import QWidget, QComboBox, QPushButton, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox")

        self.combo_box = QComboBox(self)

        # Add planets to the combo_box
        self.combo_box.addItem("Earth")
        self.combo_box.addItem("Venus")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Pluto")
        self.combo_box.addItem("Jupyter")

        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        button_set_current = QPushButton("Set value")
        button_set_current.clicked.connect(self.set_current)
        button_get_values = QPushButton("Get values")
        button_get_values.clicked.connect(self.get_values)


        # Layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_current)
        v_layout.addWidget(button_get_values)

        self.setLayout(v_layout)


    def current_value(self):
        print("Current Item : ", self.combo_box.currentText(), " ; Current Index : ",self.combo_box.currentIndex())

    def set_current(self):
        self.combo_box.setCurrentIndex(2)

    def get_values(self):
        for i in range(self.combo_box.count()):
            print("Index [",i,"] : ",self.combo_box.itemText(i))

