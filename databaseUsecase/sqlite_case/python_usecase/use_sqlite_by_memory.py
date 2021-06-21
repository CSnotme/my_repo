# -*- coding: utf-8 -*-

"""
@File        : use_sqlite_by_file.py
@Time        : 2021/6/21 23:50
@Author      : caoyf
@Tags        : <sqlite> | <python>
@Description : sqlite内存数据库的调用和操作示例
"""

import os
import sqlite3
from io import StringIO
from .use_sqlite_by_file import exists_table

"""
db_file: memory_transform_file.sqlite
table_name: demo_memory
table_desc:
    id           int primary_key autoincrement
    code         char(10) not null
    float_point  real
"""


def connect_with_memory():
    """
    sqlite打开内存数据库使用， 并写入文件sqlite
    :return:
    """

    m_table_name = "demo_memory"

    # 打开内存数据库 使用 :memory:
    m_db = sqlite3.connect(":memory:")
    mdb_cursor = m_db.cursor()
    # 执行脚本
    mdb_cursor.executescript("""
        create table {} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code char(10) NOT NULL,
            float_point real)""".format(m_table_name))
    # 插入
    mdb_cursor.execute("""insert into {} (code, float_point) values("{}", {})""".format(m_table_name, '600036', 12.0))

    # 打印表
    mdb_cursor.execute("select * from {}".format(m_table_name))
    print(mdb_cursor.fetchall())

    # 将内存中所有sql写入文件sqlite
    str_buffer = StringIO()

    for line in m_db.iterdump():
        str_buffer.write('%s\n' % line)

    # 关闭内存数据库
    m_db.close()

    current_dir = os.path.dirname(__file__)
    f_db_name = "memory_transform_file.sqlite"
    f_db_path = os.path.join(current_dir, f_db_name)

    # 打开文件数据库
    if exists_table(f_db_path, m_table_name):
        os.remove(f_db_path)
    f_db = sqlite3.connect(f_db_path)
    fdb_cursor = f_db.cursor()
    # 执行内存数据库脚本
    fdb_cursor.executescript(str_buffer.getvalue())
    # 打印表
    fdb_cursor.execute("select * from {}".format(m_table_name))
    print(fdb_cursor.fetchall())
    # 关闭文件数据库
    f_db.close()


if __name__ == '__main__':

    # 测试sqlite使用内存数据库
    connect_with_memory()
