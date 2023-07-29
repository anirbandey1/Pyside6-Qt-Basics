from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout,QGridLayout, QGroupBox, QButtonGroup, QCheckBox, QRadioButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox and QRadioButton")

        # Non-Exclusive checkboxes
        # CheckBoxes : operating system
        os = QGroupBox("Choose Operation System")

        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)
        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)
        mac = QCheckBox("Mac")
        mac.toggled.connect(self.max_box_toggled)

        # Adding Checkboxes to layout
        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)

        os.setLayout(os_layout)

        # Exclusive checkboxes
        drinks = QGroupBox("Choose your drink")

        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)

        # Add checkboxes to Button Group and Make The Button Group exclusive
        exclusive_button_group = QButtonGroup(self) # The self parent is needed here
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffee)

        exclusive_button_group.setExclusive(True)

        # Add exclusive checkboxes to layout
        drinks_layout = QVBoxLayout()
        drinks_layout.addWidget(beer)
        drinks_layout.addWidget(juice)
        drinks_layout.addWidget(coffee)

        drinks.setLayout(drinks_layout)

        # Exclusive Radio Buttons
        answers = QGroupBox("Choose your answer")
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_b.setChecked(True)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)








        widget_layout = QGridLayout()
        widget_layout.addWidget(os,0,0)
        widget_layout.addWidget(drinks,0,1)
        widget_layout.addWidget(answers,1,0)
        self.setLayout(widget_layout)

    def windows_box_toggled(self, checked):
        if (checked):
            print("Windows box checked")
        else:
            print("Windows box unchecked")

    def linux_box_toggled(self, checked):
        if (checked):
            print("Linux box checked")
        else:
            print("Linux box unchecked")

    def max_box_toggled(self, checked):
        if (checked):
            print("Mac box checked")
        else:
            print("Mac box unchecked")




