# -*- coding: utf-8 -*-
import kbengine.base as kbe
from kbengine import debug


class TestComp(kbe.EntityComponent):

    def __init__(self):
        kbe.EntityComponent.__init__(self)
