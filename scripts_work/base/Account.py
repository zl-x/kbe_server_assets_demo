# -*- coding: utf-8 -*-
import kbengine.base as kbe
from kbengine import debug
import sys

'''
    __ACCOUNT_NAME__ 
    说明：
    如果proxy是帐号则可以访问__ACCOUNT_NAME__得到帐号名。 
    
    __ACCOUNT_PASSWORD__ 
    说明：
    如果proxy是帐号则可以访问__ACCOUNT_PASSWORD__得到帐号MD5密码。 
    
    clientAddr 
    这是一个tuple对象，包含了客户端的ip与端口。 
    
    clientEnabled 
    实体是否已经可用。在实体可用之前脚本不能与客户端进行通讯。 
    
    hasClient 
    Proxy是否绑定了一个客户端连接。 
    
    roundTripTime 
    在一段时间内服务器与这个Proxy绑定的客户端通讯平均往返时间。这个属性只在Linux下生效。 
    
    timeSinceHeardFromClient 
    最后一次收到客户端数据包时到目前为止所过去的时间（秒）。 
'''


class Account(kbe.Proxy):
    def __init__(self):
        kbe.Proxy.__init__(self)
        self.avatarEntity = None

    def onClientEnabled(self):
        """
            kbe method.
            该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的cell部分。

            如果在脚本中实现了此回调，当实体可用时（ 各种初始化完毕并且可以与客户端通讯 ）该回调被调用。 这个方法没有参数。
            注意：giveClientTo将控制权赋给了该实体时也会导致该回调被调用
        """
        pass

    def sayHello(self, arg1: int, arg2: str, arg3: int) -> None:
        pass

    def reqAvatarList(self):
        pass

    def reqCreateAvatar(self, arg1: int, arg2: str) -> None:
        pass

    def reqRemoveAvatar(self, arg1: int) -> None:
        pass

    def selectAvatarEnterGame(self, arg1: int) -> None:
        pass
