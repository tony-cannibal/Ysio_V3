import sys
import os
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import *

try:
    from . import constants as cn
    from . import functions as fn
except ImportError:
    import constants as cn
    import functions as fn



class Login(QWidget):
    switch_window = QtCore.pyqtSignal(str, str, str, str)
    switch_window_user = QtCore.pyqtSignal()
    switch_window_aduana = QtCore.pyqtSignal(str)

    def __init__(self, path):
        super().__init__()
        self.root_path = path
        self.setWindowTitle('Login')
        self.setFixedSize(600, 450)

        rootlayout = QGridLayout()
        for i in [0, 2]:
            rootlayout.setColumnMinimumWidth(i, 0)
            rootlayout.setRowMinimumHeight(i, 0)
        self.setLayout(rootlayout)

        self.root_frame = QFrame()
        self.root_frame.setStyleSheet(f'''border-image: url({self.root_path}/src/blue.jpg) 
                                            0 0 0 0 stretch stretch;
                                        background-position: center;
                                        background-repeat: no-repeat; 
                                        border-radius: 6px;''')
        rootlayout.addWidget(self.root_frame, 1, 1)

        main_layout = QGridLayout()
        for i in [0, 1]:
            main_layout.setColumnMinimumWidth(i, 65)
        for i in range(0, 7):
            main_layout.setRowMinimumHeight(i, 40)
        self.root_frame.setLayout(main_layout)
        main_layout.setRowMinimumHeight(9, 100)

        label_font = QFont('Consolas', 16)
        label_font.setBold(True)

        self.line_1 = QLineEdit()
        self.line_1.setEchoMode(2)
        self.line_1.setFixedWidth(300)
        self.line_1.setAlignment(QtCore.Qt.AlignCenter)
        self.line_1.setFont(QFont('Consolas', 14))
        self.line_1.setStyleSheet('''
                background: none;
                border-image: none;
                border-style: solid;
                border-color: black;
                border-width: 1px;
                padding-top: 3px;
                padding-bottom: 3px;
                ''')
        self.label_1 = QLabel()
        self.label_1.setFixedWidth(300)
        self.label_1.setFont(label_font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setStyleSheet('''
            background: none;
            border-image: none;
            color: black;
            ''')
        self.label_1.setText('Ingresar')


        self.logo = QPixmap(f'{self.root_path}/src/logo-rojo-v2.png')
        self.label_logo = QLabel()
        self.label_logo.setStyleSheet('''
            border-style: solid;
            border-color: black;
            border-width: 0px;
            padding-right: 70px;
            border-image: none;
            background: none;
            ''')
        self.label_logo.setSizePolicy(QSizePolicy.Expanding,
                                    QSizePolicy.Expanding)
        self.label_logo.setAlignment(QtCore.Qt.AlignRight)
        self.label_logo.setPixmap(self.logo.scaled(66, 66, 
            QtCore.Qt.KeepAspectRatio))


        main_layout.addWidget(self.line_1, 8, 3, 1, 2)
        main_layout.addWidget(self.label_1, 7, 3, 1, 2)
        main_layout.addWidget(self.label_logo, 1, 3)

        self.error = QMessageBox()
        self.error.setWindowTitle('Error')
        self.error.setText('Usuario No Encontrado')
        self.error.setIcon(QMessageBox.Critical)

        self.warning = QMessageBox()
        self.warning.setWindowTitle('Advertencia')
        self.warning.setText('No Se A Detectado Ninguna Bascula')
        self.warning.setIcon(QMessageBox.Warning)


        self.line_1.returnPressed.connect(self.login)

        

    def login(self):
        query = self.line_1.text()
        area = fn.get_inv_area(query)
        user = fn.search_user(query)

        if area:
            port = fn.set_port()
            if not port:
                port = '0'
            if port == '0':
                self.warning.exec_()
            self.switch_window.emit(area[2], area[3], area[4], port)
        elif query in cn.aduana_areas:
            self.switch_window_aduana.emit(cn.aduana_areas[query][1])

        elif user:
            if query == str(user[0]):
                self.switch_window_user.emit()
        else:
            self.error.exec_()
            self.line_1.setText('')


def main():
    app = QApplication(sys.argv)

    window = Login('/'.join(os.getcwd().split('\\'))[:-5]) 
    window.setStyleSheet('''
                background: black;
                ''')
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    
    main()