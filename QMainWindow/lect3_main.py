from PySide6.QtWidgets import QApplication
from lec3_mainwindow import MainWindow

import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()