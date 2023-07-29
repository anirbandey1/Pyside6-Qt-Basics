from PySide6.QtCore import  QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar

class MainWindow (QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # declare an app window
        self.setWindowTitle("Custom Main Window")

        # Menubar and menus
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        # Edit menus
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # Other Menus
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        # Working with Toolbars
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # Add Quit action to Toolbar
        toolbar.addAction(quit_action)

        # Create our own action
        action1 = QAction("Custom Action 1", self)
        action1.setStatusTip("Status message for Custom Action 1")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("../icons/start-icon.jpg"),"Custom Action 2", self)
        action2.setStatusTip("Status Message for Custom Action 2")
        action2.triggered.connect(self.toolbar_button_click)
        # action2.setCheckable(True)
        toolbar.addAction(action2)

        # Add separator in toolbar
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Separated button"))

        # Working with Status Bar
        self.setStatusBar(QStatusBar(self))

        # Central Widget
        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)



    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        print("Custom Action 1 triggered")
        # self.statusBar().showMessage("Message from Custom Action")
        self.statusBar().showMessage("Message from Custom Action",3000)
        # 3000 is the timeout , this paramater is optional

    def button1_clicked(self):
        print("Button 1 clicked")