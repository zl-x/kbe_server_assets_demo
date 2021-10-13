# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class TestComp(KBEngine.EntityComponent):
    """
        负责运动的组件
    """

    def __init__(self):
        KBEngine.EntityComponent.__init__(self)

    def helloOnCellComp(self, arg):
        pass