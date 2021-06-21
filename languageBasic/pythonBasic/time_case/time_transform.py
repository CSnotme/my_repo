# -*- coding: utf-8 -*-

"""
@File        : time_transform.py
@Time        : 2021/6/21 23:22
@Author      : caoyf
@Tags        : <time> | <python>
@Description : 时间的获取和(timestamp, time_struct, format_time)三种时间的转换的使用示例,
"""

import datetime
import time


class TimeTools(object):

    @property
    def timestamp_now(self):
        """
        获得当前unix timestamp:1624289260.6965017
        :return: float
        """
        return time.time()

    @property
    def timestamp_now_int(self):
        """
        获得当前unix timestamp的整数:1573001316
        :return: int
        """
        return int(time.time())

    @property
    def time_struct_now(self):
        """
        获得当前时间的datetime.datetime的时间结构体
        :return: datetime.datetime
        """
        return datetime.datetime.now()

    @property
    def str_time_now(self):
        """
        获得当前时间的标准时间格式化字符串, 格式  YYYY-mm-dd HH:MM:SS
        :return: str
        """
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @property
    def str_time_now_suffix(self):
        """
        当前时间按 格式YYYYmmddHHMMSS 转换
        :return: str
        """
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    @property
    def date_str_now(self):
        """
        返回当前日期的标准字符串格式 YYYY-MM-DD
        :return: str
        """
        return datetime.datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def timestamp_to_str_time(timestamp: float):
        """
        将UNIX时间戳按本地时间转化为'2019-11-10 11:03:05' 标准时间格式化字符串
        :param timestamp:时间戳
        :return:
        """
        time_array = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', time_array)

    @staticmethod
    def timestamp_to_str_time_utc(timestamp):
        """
        将UNIX时间戳按UTC转化为'2019-11-10 11:03:05' 标准时间格式化字符串
        :param timestamp:时间戳
        :return: str
        """
        time_array = time.gmtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', time_array)

    @staticmethod
    def datetime_to_timestamp(dt: datetime.datetime):
        """
        将python datetime格式日期时间转化为UNIX时间戳(整数)
        :param dt:datetime类型
        :return: int
        """
        return int(time.mktime(dt.timetuple()))

    @staticmethod
    def str_time_to_timestamp(str_time):
        """
        将'2019-11-10 10:58:30' 标准时间格式化字符串转化为UNIX时间戳(整数)
        :param str_time:
        :return: int
        """
        time_array = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
        return int(time.mktime(time_array))

    @staticmethod
    def datetime_to_suffix(dt: datetime.datetime):
        """
        将datetime类型转换为str类型，格式为YYYYmmddHHMMSS
        :param dt: datetime
        :return: str
        """
        return dt.strftime('%Y%m%d%H%M%S')

    @staticmethod
    def str_time_to_datetime(str_time):
        """
        将'2019-11-10 11:03:05' 标准时间格式化字符串转化为 datetime类型
        :param str_time:
        :return: datetime.datetime
        """
        return datetime.datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    t = TimeTools()

    print(t.timestamp_now_int)

    print(t.str_time_now)

    print(t.date_str_now)

    print(t.str_time_now_suffix)

    print(t.str_time_to_timestamp(t.str_time_now))

    print(t.timestamp_to_str_time(t.timestamp_now))

    print(t.datetime_to_suffix(datetime.datetime(year=2020, month=1, day=1, hour=12, minute=0, second=0)))

    print(t.datetime_to_suffix(t.str_time_to_datetime('2020-01-01 22:00:00')))
