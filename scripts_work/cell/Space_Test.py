# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import sys

class Space_Test(KBEngine.Space):
    """
        Space_Test 的 cell 部分
    """

    def __init__(self):
        KBEngine.Space.__init__(self)

        INFO_MSG("cell %s over wwwwwwwwwwwwwwwwwwww" % sys._getframe().f_code.co_name)
