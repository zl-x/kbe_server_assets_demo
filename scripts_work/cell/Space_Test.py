# -*- coding: utf-8 -*-
import kbengine.cell as kbe
from kbengine import debug
import sys

class Space_Test(kbe.Space):
    """
        Space_Test 的 cell 部分
    """

    def __init__(self):
        kbe.Space.__init__(self)

        debug.INFO_MSG("cell %s over wwwwwwwwwwwwwwwwwwww" % sys._getframe().f_code.co_name)
