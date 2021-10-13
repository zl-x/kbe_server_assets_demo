# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import sys


class Space1(KBEngine.Space):
    def __init__(self):
        KBEngine.Space.__init__(self)
        # 存储在globalData中，方便获取
        KBEngine.globalData[self.__class__.__name__] = self
