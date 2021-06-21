# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import Entity_CallBack_Record


class Proxy_CallBack_Record(Entity_CallBack_Record.Entity_CallBack_Record):
    def __init__(self):
        Entity_CallBack_Record.Entity_CallBack_Record.__init__(self)

    '''
        proxy 事件回调
    '''

    def onClientDeath(self):
        '''
            如果在脚本中实现了此回调，这个方法将在客户端断开连接时被调用。 这个方法没有参数
        '''
        pass

    def onClientGetCell(self):
        '''
            如果在脚本中实现了此回调，当客户端能够调用实体的cell属性时，该回调被调用
        '''
        pass

    def onClientEnabled(self):
        """
            KBEngine method.
            该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的cell部分。

            如果在脚本中实现了此回调，当实体可用时（ 各种初始化完毕并且可以与客户端通讯 ）该回调被调用。 这个方法没有参数。
            注意：giveClientTo将控制权赋给了该实体时也会导致该回调被调用
        """
        Space1 = KBEngine.globalData["Space1"]
        self.createCellEntity(Space1.cell)

    def onGiveClientToFailure(self):
        '''
            如果在脚本中实现了此回调，当实体调用giveClientTo失败时，该回调被调用。这个方法没有参数
        '''
        pass

    def onLogOnAttempt(self, ip, port, password):
        '''
            如果在脚本中实现了此回调，这个函数在客户端尝试使用当前账号实体进行登录时触发回调。
            这种情况通常是实体存在于内存中处于有效状态，最明显的例子是用户A使用此账号登录了，用户B使用同一账号进行登录，此时回调触发。

            这个回调函数可以返回如下常量值：
            KBEngine.LOG_ON_ACCEPT：允许新的客户端与实体进行绑定，如果实体已经绑定了一个客户端，之前的客户端将被踢出。
            KBEngine.LOG_ON_REJECT：拒绝新的客户端与实体绑定。
            KBEngine.LOG_ON_WAIT_FOR_DESTROY：等待实体销毁后再进行客户端绑定。


            参数：
                ip  尝试登录的客户端IP地址。
                port  尝试登录的客户端连接的端口。
                password  用户登录时使用的MD5密码。
        '''
        return KBEngine.LOG_ON_ACCEPT

    def onStreamComplete(self, id, success):
        '''
            如果在脚本中实现了此回调，当用户使用Proxy.streamStringToClient()或Proxy.streamFileToClient()完成时，该回调被调用。
            参数：
                id  与下载关联的id。
                success  成功与否。
        '''
        pass