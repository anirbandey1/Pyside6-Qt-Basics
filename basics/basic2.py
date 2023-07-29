# Version 1 :  Setting everything in global scope

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first window app")

button = QPushButton()
button.setText("Press me")

window.setCentralWidget(button);

window.show()
app.exec()
