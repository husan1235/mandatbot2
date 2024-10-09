from os import link
from sqlite3 import Error
import sqlite3
from time import ctime


def post_sql_query(sql_query):
    with sqlite3.connect('my.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
        except Error:
            pass
        result = cursor.fetchall()
        return result


def create_tables():
    users_query = '''CREATE TABLE IF NOT EXISTS USERS
                        (user_id INTEGER PRIMARY KEY NOT NULL,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        reg_date TEXT);'''

    post_sql_query(users_query)


def create_OTM():
    otm = '''CREATE TABLE "OTM" (
	"id"	INTEGER,
	"viloyat"	TEXT,
	"yonalish"	TEXT,
	"kvota"	TEXT,
	"grant"	TEXT,
	"kontr"	TEXT,
	"link"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);'''
    post_sql_query(otm)


def register_user(user, username, first_name, last_name):
    user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO USERS (user_id, username, first_name,  last_name, reg_date) VALUES ' \
                             f'({user}, "{username}", "{first_name}", "{last_name}", "{ctime()}");'
        post_sql_query(insert_to_db_query)


def register_channel(channel_id, channel_name, channel_username, couunt):
    user_check_query = f'SELECT * FROM CHANNELS WHERE channel_id = {channel_id};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO CHANNELS (channel_id, channel_username, channel_name,  couunt) VALUES ' \
                             f'({channel_id}, "{channel_username}", "{channel_name}", "{couunt}");'
        post_sql_query(insert_to_db_query)
    else:
        a = '5'
        return a


def register_OTM(viloyat, link, yonalish, kvota, grant, kontr):
    user_check_query = f'SELECT * FROM OTM WHERE viloyat = "{viloyat}" AND yonalish="{yonalish}" AND link = "{link}" ;'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO OTM (viloyat, link, yonalish, kvota, grant, kontr) VALUES ' \
                             f'("{viloyat}", "{link}", "{yonalish}", "{kvota}", "{grant}", "{kontr}");'
        post_sql_query(insert_to_db_query)


def UPDATE_OTM(link, yonalish, kvota):
    user_check_query = f'SELECT * FROM OTM WHERE yonalish="{yonalish}" AND link = "{link}" ;'
    user_check_data = post_sql_query(user_check_query)
    if user_check_data:
        sql = f"UPDATE OTM SET kvota = '{kvota}', City= 'Frankfurt' WHERE yonalish='{yonalish}' AND link = '{link}';"


def AllUserID():
    return post_sql_query('SELECT * FROM USERS WHERE is_blocked=0')


def get_user_data(user):
    return post_sql_query(f'SELECT * FROM USERS WHERE user_id={user}')


def Block_user(cid):
    post_sql_query(f"UPDATE USERS SET is_blocked=1 WHERE user_id={cid}")


def Unblock(cid):
    post_sql_query(f"UPDATE USERS SET is_blocked=0 WHERE user_id={cid}")


def channel_ids():
    lis = []
    result = post_sql_query('SELECT channel_id FROM CHANNELS')
    for x in result:
        lis.append(x[0])
    return lis


def OTM(name, num2, ball):
    # print(f"{name}, {num2}, {ball}")
    print(f"Max={num2}, MIN={num2 - 10}")
    return post_sql_query(f"SELECT * FROM OTM WHERE {name} <= {ball} AND {name} !='-' LIMIT {num2} , 10")


def OTMCOUNT(types, ball):
    return post_sql_query(f"SELECT count(*) FROM OTM WHERE {types} <= {ball} AND {types} !='-'")[0][0]


def Votm(v, num2):
    return post_sql_query(f"SELECT * FROM OTM WHERE oViloyat='{v}'")


def V_to_Yotm(idd, num2):
    lis = []
    lisID = []
    v = post_sql_query(f"SELECT * FROM OTM WHERE id={idd}")[0][1]
    print(num2)
    a = post_sql_query(f"SELECT * FROM OTM WHERE viloyat='{v}' LIMIT {num2} , 10")
    for x in a:
        lis.append(x[2])
        lisID.append(x[0])
    return lis, lisID


def Yotm(num2):
    return post_sql_query(f"SELECT * FROM OTM LIMIT 10 OFFSET {num2}")


def Fotm(text):
    lis = []
    lisID = []
    a = post_sql_query(f"SELECT * FROM OTM WHERE yonalish LIKE '%{text}%'")
    for x in a:
        if x[8] not in lis:
            lis.append(x[8])
            lisID.append(x[0])
    return lis, lisID


def infoOTM(idd):
    return post_sql_query(f"SELECT * FROM OTM WHERE id='{idd}'")

def select_test_all():
    return post_sql_query('SELECT * FROM testlar')


def delete_tests():
    post_sql_query(f'DELETE FROM testlar')


def add_test(fmid, mid):
    insert_to_db_query = f'INSERT INTO testlar (fmid,mid) VALUES ' \
                         f'({fmid}, "{mid}");'
    post_sql_query(insert_to_db_query)

create_tables()
create_OTM()
