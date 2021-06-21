# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class Avatar(KBEngine.Proxy):
    def __init__(self):
        KBEngine.Proxy.__init__(self)
        self.accountEntity = None

    def setAccountEntity(self, accountEntity):
        self.accountEntity = accountEntity

    def destroySelf(self):
        '''
            清理流程一般是, 有 cell 部分, 则清理 cell, 在 cell 清理完成的回调中, 再 detroy

            否则直接 destroy
        '''

        # 有客户端部分, 则不
        if self.client is not None:
            return

        if self.cell:
            # 销毁cell实体
            self.destroyCellEntity()
        else:
            self.destroy()
    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------

    '''
        entity 事件回调
    '''
    def onCreateCellFailure(self):
        '''
            如果这个函数在脚本中有实现，这个函数在cell实体创建失败的时候被调用。这个函数没有参数。
        '''
        pass

    def onDestroy(self):
        """
            如果这个函数在脚本中有实现，这个函数在调用Entity.destroy()后，在实际销毁之前被调用。这个函数没有参数。
        """
        DEBUG_MSG("account::onDestroy: %i." % self.id)

    def onGetCell(self):
        '''
            如果这个函数在脚本中有实现，这个函数在它获得cell实体的时候被调用。这个函数没有参数。
        '''
        pass

    def onLoseCell(self):
        '''
            如果这个函数在脚本中有实现，这个函数在它关联的cell实体销毁之后被调用。这个函数没有参数。
        '''

        self.destroy()
        pass

    def onPreArchive(self):
        '''
            如果这个函数在脚本中有实现，这个函数在该实体自动写入数据库之前被调用。这个回调在Entity.onWriteToDB回调之前被调用。
            如果该回调返回False，该归档操作中止。这个回调应该返回True使得操作继续。如果这个回调不存在，则归档操作继续进行
        '''
        return True

    def onRestore(self):
        '''
            如果这个函数在脚本中有实现，这个函数在Entity应用程序崩溃后在其它Entity应用程序上重新创建该实体时被调用。这个函数没有参数。
        '''
        pass

    def onTimer(self, timerHandle, userData):
        """
            这个函数当一个与此实体关联的定时器触发的时候被调用。一个定时器可以使用Entity.addTimer函数添加。
            参数：
                timerHandle 定时器的id。
                userData 传进Entity.addTimer的integer用户数据。

            定时器的 id 便于删除
            用户数据用于分辨定时器
        """
        DEBUG_MSG(id, userArg)

    def onTeleportFailure(self):
        '''
            如果这个函数在脚本中有实现，当用户调用Entity.teleport失败时该回调被调用


            def teleport( self, baseEntityMB ):

                teleport会瞬移这个实体的cell部分到参数指定的实体所在的空间。

                在抵达新的空间后，Entity.onTeleportSuccess被调用。这可以用来在新的空间里移动该实体到合适的位置。
                参数： baseEntityMB 实体应该移到的指定实体所在的空间，baseEntityMB即指定实体的EntityCall。
                当成功的时候，与此参数相关联的cell实体会被传入到Entity.onTeleportSuccess函数。
        '''
        pass

    def onTeleportSuccess(self, nearbyEntity):
        '''
            如果这个函数在脚本中有实现，当用户调用Entity.teleport成功时该回调被调用。
            参数：
                nearbyEntity  这个参数由用户调用 Entity.teleport时给出。这是一个real实体
        '''
        pass

    def onWriteToDB(self, cellData):
        '''
            如果这个函数在脚本中有实现，这个函数在实体数据将要写进数据库的时候被调用。

            需要注意的是在该回调里调用writeToDB会导致无限循环。
            参数：
                cellData 包含将要存进数据库的cell属性。 cellData是一个字典。
        '''
        pass

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