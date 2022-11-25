import mysql.connector
import serial
import serial.tools.list_ports

try:
    from . import constants as cn
except ImportError:
    import constants as cn



def set_port():
    ports = []
    for i in serial.tools.list_ports.comports():
        ports.append(i[0])
    port = ''
    for i in ports:
        ser = serial.Serial(
            port=i,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1,
            write_timeout=1
        )
        ser.write('P'.encode('ascii'))
        ser_bytes = ser.read(8)
        if ser_bytes:
            port = i
        # print(i)
        # print(ser_bytes.decode('ascii'))
        ser.close()
    return port


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
    q = query.find('Q')
    res = []
    for i in data:
        if i[1] in query[:q]:
            if len(i[1]) > 4:
                res.append(i)
        if query in i[2].lower():
            res.append(i)

    # for i in res:
    #     print(i)
    return res


def get_materiales():
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('SELECT * FROM materiales;')
    res = cur.fetchall()
    con.close()
    return res


def search_selection(yura, barra):
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('''SELECT * FROM materiales WHERE provedor = %s
        AND yura = %s;
        ''', (barra, yura))
    res = cur.fetchone()
    cur.close()
    con.close()
    return res

def get_inv_area(query):
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor(buffered=True)
    cur.execute('SELECT * FROM areas_inventario where codigo = %s;', (query,))
    res = cur.fetchone()
    cur.close()
    con.close()
    return res

if __name__ == "__main__":
    code = '42102110M111C1'
    print(get_inv_area(code))
