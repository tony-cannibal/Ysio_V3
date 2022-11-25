import sys 
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import *
from datetime import date
import configparser

try:
    from . import functions as fn
    from . import constants as cn
except ImportError:
    import functions as fn
    import constants as cn


class Aduana(QWidget):
    def __init__(self, area):
        super().__init__()
        config = configparser.ConfigParser()
        config.read('sio.ini')

        self.area = area
        self.enter_history = fn.get_enter_history(self.area)
        self.exit_history = fn.get_exit_history(self.area)
        self.today = [ int(i) for i in str(date.today()).split('-') ]

        self.setWindowTitle("Aduana")
        self.setMinimumSize(800, 400)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.tab_widget = QTabWidget(self)
        self.tab1 = QWidget()
        tab1_layout = QGridLayout()
        self.tab1.setLayout(tab1_layout)

        # Tab1 Widgets
        self.line_1 = QLineEdit()
        self.line_1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.line_1.setFixedSize(160, 30)
        self.table_1 = QTableWidget()
        self.table_1.setColumnCount(10)

        self.table_1.setColumnWidth(0, 200)
        for i in [4, 5, 7, 8]:
            self.table_1.setColumnWidth(i, 200)

        # self.table_1.horizontalHeader().setStyleSheet('::section{Background-color:rgb(197, 197, 197)}')
        # self.table_1.verticalHeader().setStyleSheet('::section{Background-color:rgb(197, 197, 197)}')

        self.table_1.setHorizontalHeaderLabels(["Codigo", "Lote", "Circuito", "Tabla", 
                                                "Fecha de Entrada", "Hora de Entrada", 
                                                "Estado", "Fecha de Salida", "Hora de Salida", 
                                                "Area"])
        self.table_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_1.setAlternatingRowColors(True)

        self.radio_1 = QRadioButton("Entrada")
        self.radio_2 = QRadioButton("Salida")

        # Spacers
        self.spacer1 = QSpacerItem(30, 30, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.spacer2 = QSpacerItem(60, 30, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.spacer3 = QSpacerItem(30, 50, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.spacer4 = QSpacerItem(100, 30, QSizePolicy.Expanding, QSizePolicy.Fixed)


        # Add Widgets To Layout 1
        tab1_layout.addWidget(self.line_1, 1, 1)
        tab1_layout.addWidget(self.radio_1, 1, 2)
        tab1_layout.addWidget(self.radio_2, 1, 3)
        tab1_layout.addWidget(self.table_1, 3, 1, 1, 4)

        # Add Spacers to Layout 1
        tab1_layout.addItem(self.spacer1, 1, 4)
        tab1_layout.addItem(self.spacer1, 0, 4)
        tab1_layout.addItem(self.spacer1, 2, 4)
        tab1_layout.addItem(self.spacer2, 0, 0, 4, 1)
        tab1_layout.addItem(self.spacer2, 0, 5, 4, 1)
        tab1_layout.addItem(self.spacer3, 4, 2, 3, 1)

##########################################################################
        # Tab 2
        self.tab2 = QWidget()
        tab2_layout = QGridLayout()
        self.tab2.setLayout(tab2_layout)

        self.line_2 = QLineEdit()
        self.line_2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.date_1 = QDateTimeEdit(calendarPopup=True)
        # bqdate = QtCore.QDate.fromString(self.today, "yyyy-mm-dd")
        self.date_1.setDate(QDate(self.today[0], self.today[1], self.today[2]))
        self.date_1.setDisplayFormat('yyyy-MM-dd')

        self.date_2 = QDateTimeEdit(calendarPopup=True)
        # bqdate = QtCore.QDate.fromString(self.today, "yyyy-mm-dd")
        self.date_2.setDate(QDate(self.today[0], self.today[1], self.today[2]))
        self.date_2.setDisplayFormat('yyyy-MM-dd')
        self.date_2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.radio_3 = QRadioButton("Fecha")


        self.line_2.setFixedSize(160, 30)

        self.table_2 = QTableWidget()
        self.table_2.setColumnCount(10)
        self.table_2.setColumnWidth(0, 200)
        for i in [4, 5, 7, 8]:
            self.table_2.setColumnWidth(i, 200)

        # self.table_2.horizontalHeader().setStyleSheet('::section{Background-color:rgb(197, 197, 197)}')
        # self.table_2.verticalHeader().setStyleSheet('::section{Background-color:rgb(197, 197, 197)}')

        self.table_2.setHorizontalHeaderLabels(["Codigo", "Lote", "Circuito", "Tabla", 
                                                "Fecha de Entrada", "Hora de Entrada", 
                                                "Estado", "Fecha de Salida", "Hora de Salida", 
                                                "Area"])
        self.table_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_2.setAlternatingRowColors(True)
        # for i in range(10):
        #     self.table_2.horizontalHeaderItem(i).setFont(QFont('Arial Black', 14))

        tab2_layout.addWidget(self.table_2, 3, 1, 1, 6)
        tab2_layout.addWidget(self.date_1, 1, 3, 1, 1)
        tab2_layout.addWidget(self.date_2, 1, 4, 1, 1)
        tab2_layout.addWidget(self.radio_3,1, 2)
        tab2_layout.addWidget(self.line_2, 1, 1)



        tab2_layout.addItem(self.spacer4, 1, 5)
        tab2_layout.addItem(self.spacer4, 1, 6)
        tab2_layout.addItem(self.spacer1, 0, 4)
        tab2_layout.addItem(self.spacer1, 2, 4)
        tab2_layout.addItem(self.spacer2, 0, 0, 4, 1)
        tab2_layout.addItem(self.spacer2, 0, 7, 4, 1)
        tab2_layout.addItem(self.spacer3, 4, 2, 3, 1)



        
        self.tab_widget.addTab(self.tab1, "Aduana")
        self.tab_widget.addTab(self.tab2, "Busqueda")
        
        
        layout.addWidget(self.tab_widget)

#####################################################################
        
        #Connections 
        self.line_1.returnPressed.connect(self.aduana) 
        self.radio_1.toggled.connect(self.radio_toggle)        

        self.line_2.returnPressed.connect(self.history_search)

#####################################################################

        # Defgault States
        self.radio_1.setChecked(True)
        self.line_1.setFocus()
        self.update_entry_table()

#####################################################################
  
    def update_entry_table(self):
        self.table_1.setRowCount(len(self.enter_history))
        row_labels = []
        tablerow = 0
        for row in self.enter_history:
            self.table_1.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.table_1.item(tablerow, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.table_1.item(tablerow, 1).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.table_1.item(tablerow, 2).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.table_1.item(tablerow, 3).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4].strftime('%Y-%m-%d')))
            self.table_1.item(tablerow, 4).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.table_1.item(tablerow, 5).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.table_1.item(tablerow, 6).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.table_1.item(tablerow, 7).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            self.table_1.item(tablerow, 8).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.table_1.item(tablerow, 9).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setRowHeight(tablerow, 24)
            tablerow += 1
        for i in range(len(self.enter_history)):
            row_labels.append(str(i + 1) + " ")
        self.table_1.setVerticalHeaderLabels(row_labels)

    def update_exit_table(self):
        self.table_1.setRowCount(len(self.exit_history))
        row_labels = []
        tablerow = 0
        for row in self.exit_history:
            self.table_1.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.table_1.item(tablerow, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.table_1.item(tablerow, 1).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.table_1.item(tablerow, 2).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.table_1.item(tablerow, 3).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4].strftime('%Y-%m-%d')))
            self.table_1.item(tablerow, 4).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.table_1.item(tablerow, 5).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.table_1.item(tablerow, 6).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.table_1.item(tablerow, 7).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            self.table_1.item(tablerow, 8).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.table_1.item(tablerow, 9).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_1.setRowHeight(tablerow, 24)
            tablerow += 1
        for i in range(len(self.exit_history)):
            row_labels.append(str(i + 1) + " ")
        self.table_1.setVerticalHeaderLabels(row_labels)

    def update_search_table(self, data):
        self.table_2.setRowCount(len(data))
        row_labels = []
        tablerow = 0 
        for row in data:
            self.table_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.table_2.item(tablerow, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.table_2.item(tablerow, 1).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.table_2.item(tablerow, 2).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.table_2.item(tablerow, 3).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4].strftime('%Y-%m-%d')))
            self.table_2.item(tablerow, 4).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.table_2.item(tablerow, 5).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_2.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.table_2.item(tablerow, 6).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_2.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.table_2.item(tablerow, 7).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_2.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            self.table_2.item(tablerow, 8).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_2.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.table_2.item(tablerow, 9).setTextAlignment(QtCore.Qt.AlignCenter)
            tablerow += 1
        for i in range(len(data)):
            row_labels.append(str(i + 1) + " ")
        self.table_2.setVerticalHeaderLabels(row_labels)




    def aduana(self):
        code = self.line_1.text()
        if code[0] == '!' and code[-1] == ';' and code[11] == ';' and code[-5] == ';':
            query = fn.read_code(code)
            self.line_1.setText('')

            ### Entrada ###
            if self.radio_1.isChecked():
                if not fn.check_db(code):
                    fn.save_circuit(query, self.area)
                    self.enter_history.append(fn.check_db(code))
                    self.update_entry_table()
                else:
                    enter_error = QMessageBox()
                    enter_error.setWindowTitle('Error')
                    enter_error.setText('Este Circuito ya Fue Recolectado')
                    enter_error.exec_()
            ### Salida ###
            else:
                if fn.check_db(code):
                    circuito = fn.check_db(code)
                    if circuito[6] != cn.estados[1]:
                        fn.exit_circuit(code)
                        self.exit_history.append(fn.check_db(code))
                        self.update_exit_table()
                    else:
                        exit_error = QMessageBox()
                        exit_error.setWindowTitle('Error')
                        exit_error.setText(f'Este Cicuito salio el\n {circuito[7]} a las \n{circuito[8]}')
                        exit_error.exec_()
                else:
                    exit_error_1 = QMessageBox()
                    exit_error_1.setWindowTitle('Error')
                    exit_error_1.setText('El Circuito Aun No Se\n A Recolectado')
                    exit_error_1.exec_()
        else:
            self.line_1.setText('')
            print('codigo no valido')

    def radio_toggle(self):
        if self.radio_1.isChecked():
            self.update_entry_table()
        else:
            self.update_exit_table()

    def history_search(self):
        query = self.line_2.text()
        date_1 = self.date_1.date().toPyDate()
        date_2 = self.date_2.date().toPyDate()
        if not(self.radio_3.isChecked()):
            res = fn.search_full_hist(query)
            self.update_search_table(res)

        else:
            res = fn.search_enter_date_hist(query, date_1, date_2)
            self.update_search_table(res)



        
        
def main():
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    with open('style.qss', 'r') as f:
        style = f.read()
    app.setStyleSheet(style)


    window = Aduana('M1') 
    window.show()
    window.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    
    main()