# -*- coding: utf-8 -*-
import kbengine.base as kbe
from kbengine import debug


class Avatar(kbe.Proxy):
    def __init__(self):
        kbe.Proxy.__init__(self)
        self.accountEntity = None

    def setAccountEntity(self, accountEntity):
        self.accountEntity = accountEntity

    def onClientEnabled(self):
        """
            kbe method.
            该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的cell部分。

            如果在脚本中实现了此回调，当实体可用时（ 各种初始化完毕并且可以与客户端通讯 ）该回调被调用。 这个方法没有参数。
            注意：giveClientTo将控制权赋给了该实体时也会导致该回调被调用
        """

        debug.ERROR_MSG("avatar onClientEnabled")

    def onDestroy(self):
        debug.ERROR_MSG("avatar onDestroy")

    def giveClinetToAccountEntity(self):
        if self.accountEntity:
            self.giveClientTo(self.accountEntity)

    def entrySpace1(self):
        if self.hasClient:
            self.createCellEntity(kbe.globalData["Space1"].cell)
