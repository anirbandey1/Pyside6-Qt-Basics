from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")

        # QPushButton Hard, Critical, Question, Information, Warning
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        # Set layout
        layout = QVBoxLayout()

        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)

        self.setLayout(layout)





    # Hard way
    def button_clicked_hard(self):
        print("Button-Hard clicked")
        message = QMessageBox()
        message.setMinimumSize(700,300)
        message.setWindowTitle("Message Title")
        message.setText("Something happened to button hard")
        message.setInformativeText("Do you want to do something about it")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok :
            print("User chose Ok")
        elif ret == QMessageBox.Cancel :
            print("User chose Cancel")
        else:
            print("User chose unknown button")

    # Easy way
    def button_clicked_critical(self):
        print("Button-Critical clicked")
        ret = QMessageBox.critical(self,"Message Title", "Critical Message!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok :
            print("User chose Ok")
        elif ret == QMessageBox.Cancel :
            print("Use chose Cancel")
    def button_clicked_question(self):
        print("Button-Question clicked")

        ret = QMessageBox.question(self, "Message Title", "Question Message!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("User chose Ok")
        elif ret == QMessageBox.Cancel:
            print("Use chose Cancel")

    def button_clicked_information(self):
        print("Button-Information clicked")


        ret = QMessageBox.information(self, "Message Title", "Information Message!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("User chose Ok")
        elif ret == QMessageBox.Cancel:
            print("Use chose Cancel")

    def button_clicked_warning(self):
        print("Button-Warning clicked")

        ret = QMessageBox.warning(self, "Message Title", "Warning Message!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("User chose Ok")
        elif ret == QMessageBox.Cancel:
            print("Use chose Cancel")
    def button_clicked_about(self):
        print("Button-About clicked")

        ret = QMessageBox.about(self, "Message Title", "About Message!")

        if ret == QMessageBox.Ok:
            print("User chose Ok")
        elif ret == QMessageBox.Cancel:
            print("Use chose Cancel")
