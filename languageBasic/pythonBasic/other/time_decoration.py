# -*- coding: utf-8 -*-

"""
@File        : time_decoration.py
@Time        : 2021/6/21 19:02
@Author      : caoyf
@Tags        : python

@Description : 时间装饰器
"""

import time


def print_record_time(func):
    """
    记录函数执行时间并打印
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        use_time = time.time() - start_time
        print(use_time)
        return result
    return inner


def return_record_time(func):
    """
    记录函数执行时间并返回
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        use_time = time.time() - start_time
        return result, use_time
    return inner
