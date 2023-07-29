from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        button1 = QPushButton("one")
        button2 = QPushButton("two")
        button3 = QPushButton("three")
        # size policy is not set then button 3 will occupy the correct position but it will not take up the entire space
        button3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button4 = QPushButton("four")
        button5 = QPushButton("five")
        button6 = QPushButton("eight")
        button7 = QPushButton("seven")
        button1 = QPushButton("one")

        grid_layout = QGridLayout()
        grid_layout.addWidget(button1,0,0) # Inserting at Row 0 and Column 0
        grid_layout.addWidget(button2,0,1,1,2) # Last two arguments are row span and col span  takes up space equal to 1 row and 2cols
        grid_layout.addWidget(button3,1,0,2,1) # rowspan 1,  colspan = 2, Takes 1 row and 2 columns
        grid_layout.addWidget(button4,1,1)
        grid_layout.addWidget(button5,1,2)
        grid_layout.addWidget(button6,2,1)
        grid_layout.addWidget(button7,2,2)

        self.setLayout(grid_layout)



