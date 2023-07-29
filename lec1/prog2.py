# Version 2 : Signals sending values, Capture values in slots
from PySide6.QtWidgets import QApplication, QPushButton


# The slot : responds when something happens
def button_clicked(data):
    print("You clicked the button, didn't you checked : ", data)


app = QApplication()
button = QPushButton("Push me!")
button.setCheckable(True)
# Makes the button checkable. It's unchecked bu default
# Further clicks toggles between checked and unchecked states

# clicked is signal of QPushButton. It's  emitted  when you click on the button
# you wire a slot to the signal using the signal below

button.clicked.connect(button_clicked)
button.show()
app.exec()
