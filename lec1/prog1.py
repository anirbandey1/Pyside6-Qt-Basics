

# version 1  : Just responding to the button click : syntax
from PySide6.QtWidgets import QApplication, QPushButton

# The slot : responds when something happens
def button_clicked():
    print("You clicked the button didn't you")

app = QApplication()
button = QPushButton("Press me")

# clicked is a signal of the QPushButton
# Its emmitted when you click on the button
# You can wire a slot to the signal using th syntax below

button.clicked.connect(button_clicked)

button.show()
app.exec()



















# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
