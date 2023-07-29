from PySide6.QtWidgets import QWidget, QLabel, QLineEdit,QPushButton, QVBoxLayout, QHBoxLayout
class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and QLineEdit")

        # set of signals we can connect to
        label = QLabel("FullName : ")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.selectionChanged.connect(self.selection_changed)


        button = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("I am Here")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)


        self.setLayout(v_layout)




    def button_clicked(self):
        print("Fullname : ",self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        print("Text changed : ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self,old,new):
        print("Cursor Position Old : ",old,", New :",new)

    # press enter at the end of line
    def editing_finished(self):
        print("Editing Finished")

    def return_pressed(self):
        print("Return finished")
    def selection_changed(self):
        print("Selection changed : ",self.line_edit.selectedText())
