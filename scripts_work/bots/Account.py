# -*- coding: utf-8 -*-
import KBEngine
import copy
from kbengine import debug

class Account(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		debug.DEBUG_MSG("Account::__init__:%s." % (self.__dict__))

