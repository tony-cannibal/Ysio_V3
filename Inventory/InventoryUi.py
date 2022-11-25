import sys
import os
from datetime import date
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import *
try:
    from . import functions as fn
    from . import constants as cn
except ImportError:
    import functions as fn
    import constants as cn


# noinspection PyUnresolvedReferences
class Inventory(QWidget):
    def __init__(self, name, area, sub_area, port, path):
        super().__init__()

        self.name = name
        self.area = area
        self.sub_area = sub_area
        self.port = port
        self.root_path = path

        self.materials = []
        for i in fn.get_materiales():
            self.materials.append(i)

        self.current_sel = []
        self.history = []

        self.setStyleSheet('background-color: black;')

        main_grid = QGridLayout()
        self.setLayout(main_grid)
        main_grid.setColumnMinimumWidth(0, 0)
        main_grid.setColumnMinimumWidth(2, 10)
        main_grid.setColumnMinimumWidth(4, 0)
        main_grid.setRowMinimumHeight(0, 0)
        main_grid.setRowMinimumHeight(2, 0)

        self.frame_1 = QFrame()
        self.frame_1.setSizePolicy(QSizePolicy.Expanding, 
            QSizePolicy.Expanding)
        self.frame_2 = QFrame()
        self.frame_2.setSizePolicy(QSizePolicy.Expanding, 
            QSizePolicy.Expanding)

        main_grid.addWidget(self.frame_1, 1, 1)
        main_grid.addWidget(self.frame_2, 1, 3)

        grid_1 = QGridLayout()
        grid_1.setColumnMinimumWidth(0, 20)
        grid_1.setColumnMinimumWidth(1, 60)
        grid_1.setColumnMinimumWidth(3, 30)
        grid_1.setColumnMinimumWidth(4, 90)
        grid_1.setColumnMinimumWidth(5, 90)
        grid_1.setColumnMinimumWidth(6, 90)
        grid_1.setColumnMinimumWidth(7, 20)
        grid_1.setRowMinimumHeight(0, 20)
        grid_1.setRowMinimumHeight(2, 20)
        grid_1.setRowMinimumHeight(4, 20)
        #grid_1.setRowMinimumHeight(6, 40)
        #grid_1.setRowMinimumHeight(10, 20)
        grid_1.setRowMinimumHeight(21, 20)

        grid_2 = QGridLayout()
        grid_2.setColumnMinimumWidth(0, 40)
        grid_2.setColumnMinimumWidth(1, 130)
        grid_2.setColumnMinimumWidth(3, 130)
        grid_2.setColumnMinimumWidth(4, 40)
        grid_2.setRowMinimumHeight(0, 30)
        grid_2.setRowMinimumHeight(2, 20)
        grid_2.setRowMinimumHeight(7, 20)

        #########################################################################################################

        # Frame 1
        self.frame_1.setLayout(grid_1)

        if self.name == cn.areas[0] or self.name == cn.areas[7]:
            self.frame_1.setStyleSheet(cn.corte_m1)
        elif self.name == cn.areas[1]:
            self.frame_1.setStyleSheet(cn.medios_m1)
        elif self.name == cn.areas[2] or self.name == cn.areas[8]:
            self.frame_1.setStyleSheet(cn.corte_m2)
        elif self.name == cn.areas[3]:
            self.frame_1.setStyleSheet(cn.medios_m2)
        elif self.name == cn.areas[4]:
            self.frame_1.setStyleSheet(cn.batt)
        elif self.name == cn.areas[6]:
            self.frame_1.setStyleSheet(cn.materiales)
        elif self.name == cn.areas[5]:
            self.frame_1.setStyleSheet(cn.ensamble)
        else:
            self.frame_1.setStyleSheet(cn.default)

        # Frame 1 Items
        self.line_1 = QLineEdit()
        self.line_1.setFont(QFont('Consolas', 14))
        self.line_1.setStyleSheet('''
            background: white;
            border-style: solid;
            border-color: black;
            border-width: 1px;
            border-radius: 2px;
            padding-left: 6px;
            padding-right: 6px;
            ''')
        self.line_1.setSizePolicy(QSizePolicy.Expanding,
                                  QSizePolicy.Expanding)
        self.line_1.setMaximumSize(450, 50)

        self.line_2 = QLineEdit()
        self.line_2.setFont(QFont('Consolas', 14))
        self.line_2.setMaximumSize(120, 35)
        self.line_2.setAlignment(QtCore.Qt.AlignCenter)
        self.line_2.setStyleSheet('''
            background: white;
            border-style: solid;
            border-color: black;
            border-width: 1px;
            border-radius: 2px;
            ''')
        self.line_2.setSizePolicy(QSizePolicy.Expanding,
                                  QSizePolicy.Expanding)

        self.table_1 = QTableWidget()
        self.table_1.setStyleSheet(cn.theme)
        self.table_1.setMaximumSize(450, 1000)
        self.table_1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table_1.setColumnCount(3)
        self.table_1.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.table_1.setHorizontalHeaderLabels(['Yura', 'Tipo', 'Provedor'])
        self.table_1.setColumnWidth(0, 150)
        self.table_1.setColumnWidth(1, 150)
        self.table_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.label_main = QLabel()
        self.label_main.setText(f'Inventario Mensual: {self.name}')
        mainFont = QFont('Consolas', 16)
        mainFont.setBold(True)
        self.label_main.setFont(mainFont)
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setStyleSheet('''
            color: black;
            background: none;
            border-style: solid;
            border-color: black;
            border-width: 1px;
            border-radius: 2px;
            ''')
        labelFont = QFont(QFont('Consolas', 17))
        labelFont.setBold(True)

        self.label_1_1 = QLabel()
        self.label_1_1.setText('Provedor')
        self.label_1_1.setFont(QFont(labelFont))
        self.label_1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1_1.setStyleSheet('''
            background: white;
            color: red;
            border-style: solid;
            border-color: black;
            border-width: 1px;
            border-radius: 2px;
            ''')
        self.label_1_2 = QLabel()
        self.label_1_2.setText('Yura')
       
        self.label_1_2.setFont(QFont(labelFont))
        self.label_1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1_2.setStyleSheet('''
            background: white;
            color: red;
            border-style: solid;
            border-color: black;
            border-width: 1px;
            border-radius: 2px;
            ''')
        self.label_1_3 = QLabel()
        self.label_1_3.setText('Pkg')
        self.label_1_3.setFont(QFont(labelFont))
        self.label_1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1_3.setStyleSheet('''
            background: white;
            color: red;
            border-style: solid;
            border-color: black;
            border-width: 1px;
            border-radius: 2px;
            ''')

        self.label_1_4 = QLabel()
        self.label_1_4.setText('Pkg')
        self.label_1_4.setFont(QFont(labelFont))
        self.label_1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1_4.setStyleSheet('''
            background: white;
            color: red;
            border-style: solid;
            border-color: black;
            border-width: 1px;
            border-radius: 2px;
            ''')

        self.label_amount = QLabel()
        self.label_amount.setMaximumSize(120, 35)
        self.label_amount.setText('')
        self.label_amount.setFont(QFont('Consolas', 14))
        self.label_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.label_amount.setStyleSheet('''
            color: black;
            border-style: solid;
            border-color: black;
            border-width: 1px;
            border-radius: 2px;
            ''')
        radioFont = QFont('Consolas', 10)
        radioFont.setBold(True)

        self.radio1 = QRadioButton()
        self.radio1.setFont(QFont(radioFont))
        self.radio1.setText('Peso')
        self.radio1.setStyleSheet(cn.theme)
        self.radio2 = QRadioButton()
        self.radio2.setFont(QFont(radioFont))
        self.radio2.setText('Nuevo')
        self.radio2.setStyleSheet(cn.theme)
        self.radio3 = QRadioButton()
        self.radio3.setFont(QFont(radioFont))
        self.radio3.setText('Cantidad')
        self.radio3.setStyleSheet(cn.theme)

        self.button_1 = QPushButton()
        self.button_1.setText('Pesar')
        self.button_1.setMaximumSize(120, 35)
        self.button_1.setStyleSheet(cn.theme)
        self.button_1.setSizePolicy(QSizePolicy.Expanding,
                                    QSizePolicy.Expanding)

        self.box_1 = QCheckBox()
        self.box_1.setFont(QFont(radioFont))
        self.box_1.setText('Tara')
        self.box_1.setStyleSheet(cn.theme)

        self.combo = QComboBox()
        self.combo.setMaximumSize(120, 50)
        self.combo.setStyleSheet(cn.theme)
        self.combo.setFont(QFont('Consolas', 16))
        self.combo.setSizePolicy(QSizePolicy.Expanding,
                                 QSizePolicy.Expanding)

        self.logo = QPixmap(f'{self.root_path}/src/logo-rojo-v2.png')
        self.label_img = QLabel()

        self.label_img.setSizePolicy(QSizePolicy.Expanding,
                                    QSizePolicy.Expanding)
        self.label_img.setStyleSheet('''
            border-width: 0px;
            ''')
        self.label_img.setAlignment(QtCore.Qt.AlignRight)
        self.label_img.setPixmap(self.logo.scaled(66, 66, 
            QtCore.Qt.KeepAspectRatio))
        self.label_img.setMaximumSize(100, 40)

        # Add Items to Frame 1
        grid_1.addWidget(self.label_main, 1, 1, 1, 5)
        grid_1.addWidget(self.label_img, 1, 6, 1, 2)

        grid_1.addWidget(self.line_1, 3, 1, 1, 1)
        grid_1.addWidget(self.combo, 3, 6, 1, 1)

        grid_1.addWidget(self.table_1, 5, 1, 16, 2)

        grid_1.addWidget(self.label_1_1, 5, 4, 1, 3)
        grid_1.addWidget(self.label_1_2, 7, 4, 1, 3)
        grid_1.addWidget(self.label_1_3, 9, 4, 1, 3)
        grid_1.addWidget(self.label_1_4, 11, 4, 1, 3)

        grid_1.addWidget(self.radio1, 13, 4)
        grid_1.addWidget(self.radio2, 13, 5)
        grid_1.addWidget(self.radio3, 13, 6)

        grid_1.addWidget(self.box_1, 14, 4)
        grid_1.addWidget(self.line_2, 17, 4)
        grid_1.addWidget(self.button_1, 17, 6)
        grid_1.addWidget(self.label_amount, 18, 4)

        self.error = QMessageBox()
        self.error.setWindowTitle('Error')
        self.error.setText('Cantidad No Valida')
        self.error.setInformativeText("La cantidad no debe ser menor o igual a '0'.")

        self.error.setIcon(QMessageBox.Critical)

        ##########################################################################################################

        # Frame 2 Items
        self.frame_2.setLayout(grid_2)
        self.frame_2.setStyleSheet('''
            background: White;
            border-style: solid;
            border-color: black;
            border-width: 1px;
            border-radius: 8px;
            ''')

        self.label_2_1 = QLabel()
        self.label_2_1.setText('Historial de Inventario')
        self.label_2_1.setFont(QFont('Consolas', 14))
        self.label_2_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2_1.setStyleSheet(cn.theme)
        self.table_2 = QTableWidget()
        self.table_2.setStyleSheet(cn.theme)
        self.table_2.setSizePolicy(QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        self.table_2.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.table_2.setColumnCount(7)
        self.table_2.setHorizontalHeaderLabels(['Yura', 'Proveedor', 'Cantidad', 
            'Peso', 'Maquina', 'Area','Fecha'])
        self.table_2.setColumnWidth(0, 120)
        self.table_2.setColumnWidth(1, 120)
        self.table_2.setColumnWidth(2, 120)
        self.table_2.setColumnWidth(3, 120)
        self.table_2.setColumnWidth(4, 120)
        self.table_2.setColumnWidth(5, 120)
        self.table_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Add Items to Frame 2
        grid_2.addWidget(self.label_2_1, 1, 2)
        grid_2.addWidget(self.table_2, 3, 1, 4, 3)

        ###############################################################################################################

        # Set Default States
        self.radio1.setChecked(True)
        self.box_1.setChecked(True)

        ###############################################################################################################

        # Function Connections
        self.line_1.returnPressed.connect(self.search)
        self.table_1.itemSelectionChanged.connect(self.table_update_label)
        self.line_2.textChanged.connect(self.get_amount)
        self.radio2.toggled.connect(self.get_amount)
        self.box_1.toggled.connect(self.get_amount)
        self.line_2.returnPressed.connect(self.save_record)
        self.button_1.clicked.connect(self.get_weight)


        ################################################################################################################

        # Autorun Functions
        self.maquinas = fn.get_machines(self.area, self.sub_area)
        cable = self.sub_area[:5]
        if cable.lower() != 'cable':
            self.combo.addItem("")
        for i in self.maquinas:
            self.combo.addItem(i[0])

        self.search()

    ################################################################################################################

    # Declare Functions
    def search(self):
        query = self.line_1.text().lower()
        res = fn.search_mats(self.materials, query)
        if len(res) != 0:
            self.table_1.setRowCount(len(res))
            row_labels = []
            tablerow = 0
            for row in res:
                self.table_1.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[2]))
                self.table_1.item(tablerow, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                self.table_1.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[4]))
                self.table_1.item(tablerow, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                self.table_1.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
                self.table_1.item(tablerow, 2).setTextAlignment(QtCore.Qt.AlignCenter)
                self.table_1.setRowHeight(tablerow, 20)
                tablerow += 1

            for i in range(len(self.history)):
                row_labels.append(str(i + 1) + "  ")
            self.table_1.setVerticalHeaderLabels(row_labels)
            self.table_1.setCurrentCell(1, 0)
            self.table_1.setCurrentCell(0, 0)
        else:
            self.line_1.setText("")


    def table_update_label(self):
        sel = self.table_1.currentRow()
        if sel != -1:
            yura = self.table_1.item(sel, 0).text()
            barra = self.table_1.item(sel, 2).text()
            self.current_sel = list(fn.search_selection(yura, barra))
            # print(self.current_sel)
        else:
            print("No Match Found")

        if len(self.current_sel) == 9:
            self.label_1_1.setText(f'YURA: {self.current_sel[2]}')
            self.label_1_2.setText(f'{self.current_sel[3].upper()}')
            self.label_1_3.setText(f'TIPO: {str(self.current_sel[4])}')
            self.label_1_4.setText(f'PKG: {str(self.current_sel[7])}')
        self.line_1.setText("")
        self.line_2.setText("")

    def get_amount(self):
        if self.line_2.text() != '':
            simbols = ['/', '*', '-', '+', "'", ',' , '/', '?' , '"', '[', ']', '\\', '=', '-', '`', ';']
            if self.line_2.text().count('.') > 1 or self.line_2.text()[len(self.line_2.text())-1].isalpha() or self.line_2.text()[len(self.line_2.text())-1] in simbols:
                self.line_2.setText(self.line_2.text()[:-1])
            else:
                if self.radio1.isChecked():
                    if len(self.current_sel) == 0:
                        return 0
                    peso = self.line_2.text()
                    if peso == "":
                        peso = 0
                    else:
                        peso = float(peso)
                    tipo = self.current_sel[4]
                    if not self.box_1.isChecked():
                        tara = 0
                    else:
                        tara = self.current_sel[8]
                    peso_ind = self.current_sel[5]
                    resultado = fn.calc_amount(tipo=tipo, weight=peso, ind_weight=peso_ind, tara=tara)
                    self.label_amount.setText(str(resultado))
                elif self.radio2.isChecked():
                    self.label_amount.setText(str(self.current_sel[6]))
                else:
                    self.label_amount.setText(self.line_2.text())

    def save_record(self):
        try:
            if float(self.label_amount.text()) > 0:
                # provedor, yura, tipo, cantidad, peso,  area, maquina, fecha
                ob = [self.current_sel[3], self.current_sel[2], self.current_sel[4], self.label_amount.text(),
                      self.combo.currentText(), self.line_2.text(), self.name, date.today().strftime("%Y-%m-%d")]
                # print(ob)
                self.history.append(ob)
                fn.capture_value(ob)
                self.display_history()
                self.line_1.setText("")
                self.line_2.setText("")
                self.line_1.setFocus()
            else:
    
                self.error.exec_()
                # print("Peso Erroneo")
        except:
            pass

    def display_history(self):
        self.table_2.setRowCount(len(self.history))
        row_labels = []
        tablerow = 0
        # for i in self.history:
        #     print(i)
        for row in self.history:
            # Yura
            self.table_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.table_2.item(tablerow, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            # Proveedor
            self.table_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
            self.table_2.item(tablerow, 1).setTextAlignment(QtCore.Qt.AlignCenter)
            # Cantidad
            self.table_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.table_2.item(tablerow, 2).setTextAlignment(QtCore.Qt.AlignCenter)
            # peso
            self.table_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
            self.table_2.item(tablerow, 3).setTextAlignment(QtCore.Qt.AlignCenter)
            # Maquina
            self.table_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.table_2.item(tablerow, 4).setTextAlignment(QtCore.Qt.AlignCenter)
            # Area
            self.table_2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[6]))
            self.table_2.item(tablerow, 5).setTextAlignment(QtCore.Qt.AlignCenter)
            # fecha
            self.table_2.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[7]))
            self.table_2.item(tablerow, 6).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_2.setRowHeight(tablerow, 20)
            tablerow += 1
        for i in range(len(self.history)):
            row_labels.append(str(i + 1) + "  ")
        self.table_2.setVerticalHeaderLabels(row_labels)

    def get_weight(self):
        if self.port == '0':
            weight = '0'
        else:
            weight = fn.read_weight(self.port)
        self.line_2.setText('')
        self.line_2.setText(weight)
        self.line_2.setFocus()


def main():
    app = QApplication(sys.argv)

    window = Inventory('Corte M1', 'M1', 'corte', '0', '/'.join(os.getcwd().split('\\'))[:-9])
    window.showMaximized()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
