import sys
import os
import configparser
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets

from Login import LoginUi
from Inventory import InventoryUi
from User import UserUi
from Aduana import AduanaUi


class Controller:

    def __init__(self):
        self.path = '/'.join(os.getcwd().split('\\'))

    def show_login(self):
        self.login = LoginUi.Login(self.path)
        self.login.setStyleSheet('''
            background: black;
                 ''')
        self.login.switch_window.connect(self.show_main)
        self.login.switch_window_user.connect(self.show_user)
        self.login.switch_window_aduana.connect(self.show_aduana)

        self.login.show()

    def show_main(self, name, area, sub_area, port):
        self.window = InventoryUi.Inventory(name, area, sub_area, port, self.path)
        self.login.close()
        self.window.show()
        self.window.showFullScreen()

    def show_aduana(self, area):
        self.aduana = AduanaUi.Aduana(area)
        self.login.close()
        self.aduana.show()
        self.aduana.showMaximized()
    
    def show_user(self):
        self.user = UserUi.User()
        self.login.close()
        self.user.show()

    def show_feeder(self):
        pass

    def show_admin(self):
        pass


def main():
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    # with open('src/style.qss', 'r') as f:
    #     style = f.read()
    # app.setStyleSheet(style)


    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # print(sys.version)
    main()
