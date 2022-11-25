import mysql.connector
import serial

try:
    from . import constants as cn
except ImportError:
    import constants as cn


def search_user(query):
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('SELECT * FROM empleados where noreloj = %s;',
                (query,)
                )
    res = cur.fetchone()
    cur.close()
    con.close()
    if res:
        return res


def search_db(data, query):
    q = query.find('q')
    res = []
    for i in data:
        if i[1].lower() in query[:q]:
            if len(i[1]) > 4:
                res.append(i)
        if query in i[2].lower():
            res.append(i)
    return res


# def get_materiales():
#     con = mysql.connector.connect(**cn.db)
#     cur = con.cursor()
#     cur.execute('SELECT * FROM materiales;')
#     res = cur.fetchall()
#     con.close()
#     return res


def search_selection(yura, barra):
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('''SELECT * FROM materiales WHERE codigo_proveedor = %s
        AND codigo_yura = %s;
        ''', (barra, yura))
    res = cur.fetchone()
    cur.close()
    con.close()
    return res


def calc_amount(tipo, weight, ind_weight, tara, use_pkg=True):
        if not use_pkg:
            tara = 0
        if tipo == "sello":
            return round((weight * 1000) / ind_weight, 1)
        else:
            try:
                return round((weight - tara) / ind_weight, 1)
            except ZeroDivisionError:
                return 0
    

def get_machines(area:str, sub_area:str) -> list:
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('''
        SELECT * FROM maquinas 
        where area = %s and sub_area = %s ;
        ''', (area, sub_area)
                )
    res = cur.fetchall()
    cur.close()
    con.close()
    return res


def capture_value(item):
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('''
    INSERT INTO inventario_mensual(
        proveedor, yura, tipo,
        cantidad, peso,  area, maquina,
        fecha
    ) VALUES(
        %s, %s, %s,
        %s, %s, %s,
        %s, %s
    );
    ''', (item[0], item[1], item[2], item[3], item[5], item[6], item[4], item[7]))
    con.commit()
    con.close()


def read_weight(puerto):
    ser = serial.Serial(
        port=puerto,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1,
        write_timeout=1
    )
    ser.write('P'.encode('ascii'))
    weight = ser.read(8).decode('ascii').strip()
    return weight

def search_mats(data, query):
    query = query.upper()
    q = query.find('Q')
    res = []
    for i in data:
        if len(query) >= 20:
            if query[1:q] in i[0]:
                res.append(i)
        else:
            if query in i[0]:
                res.append(i)
    return res

def get_materiales():
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('SELECT * FROM materiales;')
    res = cur.fetchall()
    cur.close()
    con.close()
    res = [list(i) for i in res]
    for i in res:
        i[0] = f'{i[1]} {i[2]} {i[3]}' 
    return res
    
def get_inv_area(query):
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor(buffered=True)
    cur.execute('SELECT * FROM areas_inventario where codigo = %s;', (query,))
    res = cur.fetchone()
    cur.close()
    con.close()
    if res:
        return res

if __name__ == "__main__":
    item = ['AVS 8.0 R', 'WAS0800300', 'CABLE', '3.5', 'W001', '0.32', 'Cable M1', '2022-11-25']
    capture_value(item)