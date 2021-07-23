import pymysql

conn = 0
curs = 0

#DB연결
def db_connect():
    global conn, curs
    try:
        conn = pymysql.connect(host='localhost', user='sba', password='1234', db='testdb', charset='utf8')
    except:
        print("DB 연결을 실패했습니다.")
        return False
    # print(conn)
    curs = conn.cursor(pymysql.cursors.DictCursor)
    return True

#DB연결해제
def db_close():
    curs.close()
    conn.close()

# 상품 현황 확인
def show_product():
    type = int(input('1.예금\n2.적금\n3.카드\n'))
    if type == 1 :
        sql = f'select name from product where type = {type}'
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
             print('예금:', row['name'])

    elif type == 2 :
        sql = f'select name, percentage from product where type = {type}'
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            print('적금:', row['name'], row['percentage'])

    elif type == 3 :
        sql = f'select name from product where type = {type}'
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            print('카드:', row['name'])

    else:
        print('번호를 잘못 입력하셨습니다.')

if __name__ == '__main__' :
    if db_connect() == True:
        print('연결됐지롱')
    show_product()