# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/15 11:52 
@Description     ：
'''
from poos.core.TencentCos import TencentCos

tcos = TencentCos()


def SearchBucket():
    return tcos.SearchBucket()
