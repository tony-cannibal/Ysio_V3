import mysql.connector
from datetime import date, datetime
try:
    from . import constants as cn
except ImportError:
    import constants as cn


def read_code(code):
    lot, circuit, number = code[1:-1].split(';')
    return [code, lot, circuit, number]

def check_db(query):
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('SELECT * FROM aduana where codigo = %s;',
                (query,))
    res = cur.fetchone()
    cur.close()
    return res

def save_circuit(info, area):
    today = date.today().strftime('%Y-%m-%d')
    time = datetime.now().strftime("%H:%M:%S")
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('''
    INSERT INTO aduana(
        codigo, lote, circuito, tabla, fechaentrada, horaentrada, estado, area
    ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
    ''', (info[0], info[1], info[2], info[3], today, time, cn.estados[0], area))
    con.commit()
    con.close()

def exit_circuit(code):
    today = date.today().strftime('%Y-%m-%d')
    time = datetime.now().strftime("%H:%M:%S")
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('''
    UPDATE aduana
    SET estado = %s, fechasalida = %s, horasalida = %s
    WHERE codigo = %s;
    ''', (cn.estados[1], today, time, code))
    con.commit()
    con.close()

def get_enter_history(area):
    today = date.today().strftime('%Y-%m-%d')
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('SELECT * FROM aduana WHERE fechaentrada = %s and area = %s;',
                (today, area))
    res = cur.fetchall()
    cur.close()
    return res

def get_exit_history(area):
    today = date.today().strftime('%Y-%m-%d')
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('SELECT * FROM aduana WHERE fechasalida = %s and area = %s;',
                (today, area))
    res = cur.fetchall()
    cur.close()
    return res

def search_full_hist(query):
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('''
        SELECT * FROM aduana 
        WHERE lote = %s 
        OR circuito LIKE %s
        OR codigo like %s;
        ''',( '%'+query+'%', '%'+query+'%', '%'+query+'%'))
    res = cur.fetchall()
    cur.close()
    return res

def search_enter_date_hist(query, date_1, date_2):
    con = mysql.connector.connect(**cn.db)
    cur = con.cursor()
    cur.execute('''
        SELECT * FROM aduana 
        WHERE lote = %s 
        OR circuito LIKE %s
        OR codigo like %s
        ;
        ''',( '%'+query+'%', '%'+query+'%', '%'+query+'%'))
    res = [ i for i in cur.fetchall() if i[4] >= date_1 and i[4] <= date_2 ]

    # filtered_res = [ i for i in res if i[4] >= date_1 and i[4] <= date_2 ]
    cur.close()

    return res


if __name__ == '__main__':

    query = 'ef601'
    date_1 = datetime.strptime('2022-05-30', '%Y-%m-%d').date()
    date_2 = datetime.strptime('2022-06-03', '%Y-%m-%d').date()



    res = search_enter_date_hist(query, date_1, date_2)

    for i in res:
        print(i)
   