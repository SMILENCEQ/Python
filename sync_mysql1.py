# -*- coding: utf-8 -*-
"""
@Time:2025/5/29 14:38
@Auth:HEhandsome
"""
import pymysql
from pymysql import Connect


class Mysql:
    def __init__(self):
        #源数据库
        self.sou_host = 'sou_host'
        self.sou_user = 'sou_user'
        self.sou_port = 3306
        self.sou_password = 'sou_password'
        self.sou_database = 'sou_database'
        #目标数据库
        self.tag_host = 'tag_host'
        self.tag_user = 'tag_user'
        self.tag_port = 3306
        self.tag_password = 'tag_password'
        self.tag_database = 'tag_database'
        #存储表结构
        self.create_table_sql=None
        self.select_table_sql=None
        self.columns=None

        #连接源数据库和目标数据库
        self.sou_conn=pymysql.Connect(
            host=self.sou_host,
            user=self.sou_user,
            port=self.sou_port,
            password=self.sou_password,
            database=self.sou_database
        )
        self.tag_conn=pymysql.Connect(
                host=self.tag_host,
                user=self.tag_user,
                port=self.tag_port,
                password=self.tag_password,
                database=self.tag_database
        )
    def get_source_db(self):
        try:
            with self.sou_conn.cursor() as cursor:
                #获取表结构
                cursor.execute('SHOW CREATE TABLE users')
                # print(cursor.fetchone())
                result = cursor.fetchone()
                self.create_table_sql = result[1]
        except Exception as e:
            print(f'获取失败:{e}')

    def get_tag_db(self):
        with self.tag_conn.cursor() as cursor:
            cursor.execute('DROP TABLE IF EXISTS users')
            cursor.execute(self.create_table_sql)
            self.tag_conn.commit()

    def read_sou_data(self):
        with self.sou_conn.cursor() as cursor:
            #获取表结构
            cursor.execute('SELECT * FROM users')
            result = cursor.fetchall()
            self.select_table_sql = result
            #获取当前查询结果的所有列名，形成一个列表
            self.columns = [desc[0] for desc in cursor.description]  # 获取列名
    def write_tag_db(self):
        with self.tag_conn.cursor() as cursor:
            # 构建插入语句
            placeholders = ','.join(['%s'] * len(self.columns))
            cols = ','.join(self.columns)
            sql = f"INSERT INTO users ({cols}) VALUES ({placeholders})"
            #插入数据
            cursor.executemany(sql, self.select_table_sql)
            self.tag_conn.commit()
            print(f"成功插入 {cursor.rowcount} 条记录")
if __name__ == '__main__':
    db = Mysql()
    db.get_source_db()
    db.get_tag_db()
    db.read_sou_data()
    db.write_tag_db()









