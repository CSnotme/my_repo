# -*- coding: utf-8 -*-

"""
@File        : use_sqlite_by_file.py
@Time        : 2021/6/21 23:50
@Author      : caoyf
@Tags        : <sqlite> | <python>
@Description : sqlite文件数据库的调用和操作示例
"""

import os
import sqlite3

"""
db_file: demo.sqlite
table_name: demo
table_desc:
    device_name    varchar(64)
    device_status  int

"""


def exists_table(db_path, table_name):
    """
    判断是否存在表
    :param db_path:  sqlite库的绝对路径
    :param table_name: 表名
    :return: False or True
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    select_sql = '''SELECT COUNT(*) FROM sqlite_master WHERE type='table' and name="{}"'''.format(table_name)
    try:
        ret = cursor.execute(select_sql).fetchone()[0]
        if ret:
            return True
        else:
            return False
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


def create_table(db_path, table_name):
    """
    创建表
    :param db_path: 文件路径
    :param table_name: 表名
    :return:
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    create_sql = '''CREATE TABLE `{}` (device_name varchar(64), device_status int)'''.format(table_name)
    try:
        cursor.execute(create_sql)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


def insert_device_info(db_path, table_name, device_name, device_status):
    """
    插入数据
    :param db_path: sqlite库的绝对路径
    :param table_name: 表名
    :param device_name:
    :param device_status: 状态 0关闭， 1开启
    :return:
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    insert_sql = '''INSERT INTO `{}` (device_name, device_status) VALUES ("{}", {})'''.format(table_name, device_name, device_status)
    try:
        cursor.execute(insert_sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()


def update_device_status(db_path, table_name, device_name, device_status):
    """
    更新状态
    :param db_path: sqlite库的绝对路径
    :param table_name: 表名
    :param device_name:
    :param device_status: 状态 0关闭， 1开启
    :return:
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    update_sql = '''UPDATE `{}` SET device_status={} WHERE device_name="{}"'''.format(table_name, device_status, device_name)
    try:
        cursor.execute(update_sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()


def select_device_status(db_path, table_name, device_name):
    """
    查询状态
    :param db_path: sqlite库的绝对路径
    :param table_name: 表名
    :param device_name:
    :return:
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    select_sql = '''SELECT `device_status` FROM {} WHERE device_name="{}"'''.format(table_name, device_name)
    try:
        ret = cursor.execute(select_sql).fetchone()
        if ret:
            return ret[0]
        else:
            return None
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


def delete_device(db_path, table_name, device_name):
    """
    删除
    :param db_path: sqlite库的绝对路径
    :param table_name: 表名
    :param device_name:
    :return:
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    select_sql = '''DELETE FROM {} WHERE device_name="{}"'''.format(table_name, device_name)
    try:
        ret = cursor.execute(select_sql).fetchone()
        if ret:
            return ret[0]
        else:
            return None
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':

    parent_dir = os.path.dirname(__file__)

    db_name = "demo.sqlite"
    table_name = "demo"

    db_path = os.path.join(parent_dir, db_name)
    if not exists_table(db_path, table_name):
        create_table(db_path, table_name)
        insert_device_info(db_path, table_name, 'device_1', 0)
        insert_device_info(db_path, table_name, 'device_2', 0)

    # 查询
    print(select_device_status(db_path, table_name, 'device_1'))
    print(select_device_status(db_path, table_name, 'device_2'))

    # 更新并查询
    update_device_status(db_path, table_name, 'device_1', 1)
    print(select_device_status(db_path, table_name, 'device_1'))

    # 删除并查询
    delete_device(db_path, table_name, 'device_2')
    print(select_device_status(db_path, table_name, 'device_2'))
