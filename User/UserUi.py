import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import *


class User(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Usuario")
        menuBar = QMenuBar()
        self.setMenuBar(menuBar)
        fileMenu = QMenu("&File", self)

        self.button_action = QAction("&Your button", self)
        self.button_action.setStatusTip("This is your button")
        #button_action.setCheckable(True)

        fileMenu.addAction(self.button_action)
        

        menuBar.addMenu(fileMenu)
        




def main():
    app = QApplication(sys.argv)

    window = User()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    
    main()