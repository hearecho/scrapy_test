import pymysql
from scrapy_test import settings


MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'ssf971114'
MYSQL_PORT = '3306'
MYSQL_DB = 'novel_scrapy'

db = pymysql.connect(MYSQL_HOSTS,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DB,charset="utf8")
cursor = db.cursor()
class Sql:
    @classmethod
    def insert_dd_name(cls,xs_name,xs_author,category,name_id):
        sql = 'INSERT INTO dd_name(xs_name,xs_author,category,name_id) VALUES (\'{}\',\'{}\',\'{}\',\'{}\')'.format(xs_name,xs_author,category,name_id)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e.args)
            db.rollback()

    @classmethod
    def select_name(cls,name_id):
        sql = "select * from dd_name WHERE name_id = {}".format(name_id)
        # value ={
        #     'name_id':name_id
        # }
        cursor.execute(sql)
        if not cursor.fetchall():
            return 0
        else:
            return 1
