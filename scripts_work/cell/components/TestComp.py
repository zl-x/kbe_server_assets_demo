# -*- coding: utf-8 -*-
import kbengine.cell as kbe
from kbengine import debug


class TestComp(kbe.EntityComponent):
    """
        负责运动的组件
    """

    def __init__(self):
        kbe.EntityComponent.__init__(self)

    def helloOnCellComp(self, arg):
        pass