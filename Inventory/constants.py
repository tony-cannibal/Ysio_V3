db = {
        'host': '172.18.4.58',
        'database': 'yura_elaboracion',
        'user': 'yura_admin',
        'password': 'Metallica24+'}

db2 = {
    'host': '172.18.4.51',
    'database': 'yuracorporation',
    'user': 'yurano',
    'password': 'yuracorporation4200'
}



areas = ['Corte M1', 'Medios M1', 'Corte M2', 'Medios M2', 'BATTERY', 'ENSAMBLE', 'MATERIALES ALMACEN', 'Cable M1', 'Cable M2']



# Area Styles
corte_m1 = '''
    background: rgb(37, 186, 35);
    border-style: solid;
    border-color: black;
    border-width: 1px;
    border-radius: 8px;
'''
corte_m2 = '''
    background: rgb(163, 46, 231);
    border-style: solid;
    border-color: black;
    border-width: 1px;
    border-radius: 8px;
'''
medios_m1 = '''
    background: rgb(255, 160, 8);
    border-style: solid;
    border-color: black;
    border-width: 1px;
    border-radius: 8px;
'''
medios_m2 = '''
    background: rgb(66, 126, 255);
    border-style: solid;
    border-color: black;
    border-width: 1px;
    border-radius: 8px;
'''
batt = '''
    background: rgb(66, 126, 255);
    border-style: solid;
    border-color: black;
    border-width: 1px;
    border-radius: 8px;
'''

materiales = '''
    background: rgb(222, 207, 38);
    border-style: solid;
    border-color: black;
    border-width: 1px;
    border-radius: 8px;
'''

ensamble = '''
    background: rgb(255, 106, 231);
    border-style: solid;
    border-color: black;
    border-width: 1px;
    border-radius: 8px;
'''

default = '''
    background: white;
    border-style: solid;
    border-color: black;
    border-width: 1px;
    border-radius: 8px;
'''


theme = '''
    
    QPushButton{
        background-color: #fff;
        color: #000;
        border-radius: 2px;
    }

    QPushButton::pressed {
        color: white;
        background-color: black;
    }

    QLabel {
        color: black;
        border-width: 0px;
    }

    QLineEdit {
        color: black;
    }

    QComboBox {
        background-color: #fff;
        border-radius: 1px;
        border-style: solid;
        border-color: black;
        padding-left: 20px;
    }

    QComboBox QAbstractItemView {
        background-color: #fff;
        selection-color: #000;
        selection-background-color: #000;
    }

    QRadioButton, QCheckBox{
        border-width: 0px;
    }

    QTableWidget {
        background-color: #fff;
        border-radius: 1px;
    }

    QHeaderView {
        border-radius: 1px;
    }

    QScrollBar {
        background-color: #fff;
        
    }

   '''