#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: keyboard_action.py
@time: 2020/8/31 14:32
@desc: 处理键盘
"""

from pykeyboard import *
from tip_time import TipTime


class KeyboardAction:
    def __init__(self):
        self.k = PyKeyboard()
        self.t = TipTime()

    def key_input(self, str='test'):
        """输入内容"""
        self.k.type_string(str)
        self.t.tip()
