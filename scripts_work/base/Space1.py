# -*- coding: utf-8 -*-
import kbengine.base as kbe
from kbengine import debug
import sys


class Space1(kbe.Space):
    def __init__(self):
        kbe.Space.__init__(self)
        # 存储在globalData中，方便获取
        kbe.globalData[self.__class__.__name__] = self
