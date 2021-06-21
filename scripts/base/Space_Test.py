# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import sys


class Space_Test(KBEngine.Space):
    """
        Space_Test 的 base 部分，
        注意：它是一个实体，并不是真正的space，真正的space存在于cellapp的内存中，通过这个实体与之关联并操控space。
    """

    def __init__(self):
        KBEngine.Space.__init__(self)
        # 存储在globalData中，方便获取
        KBEngine.globalData[self.__class__.__name__] = self

        INFO_MSG("base %s over wwwwwwwwwwwwwwwwwwww" % sys._getframe().f_code.co_name)