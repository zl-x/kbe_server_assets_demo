# -*- coding: utf-8 -*-
import kbengine.base as kbe
from kbengine import debug


class FirstSpace(kbe.Space):
    """
    FirstSpace的base部分，
    注意：它是一个实体，并不是真正的space，真正的space存在于cellapp的内存中，通过这个实体与之关联并操控space。
    """

    def __init__(self):
        kbe.Space.__init__(self)
        # 存储在globalData中，方便获取
        kbe.globalData["FirstSpace"] = self
