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

        debug.DEBUG_MSG(dir(self))

        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))

        # 顶号时使用, 其他时间都是为 None
        self.avatarEntity = None

    def onCreateCellFailure(self):
        '''
            如果这个函数在脚本中有实现，这个函数在cell实体创建失败的时候被调用。这个函数没有参数。
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
        pass

    def onDestroy(self):
        """
            如果这个函数在脚本中有实现，这个函数在调用Entity.destroy()后，在实际销毁之前被调用。这个函数没有参数。
        """
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))

    def onGetCell(self):
        '''
            如果这个函数在脚本中有实现，这个函数在它获得cell实体的时候被调用。这个函数没有参数。
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
        pass

    def onLoseCell(self):
        '''
            如果这个函数在脚本中有实现，这个函数在它关联的cell实体销毁之后被调用。这个函数没有参数。
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))

        self.destroy()

        pass

    def onPreArchive(self):
        '''
            如果这个函数在脚本中有实现，这个函数在该实体自动写入数据库之前被调用。这个回调在Entity.onWriteToDB回调之前被调用。
            如果该回调返回False，该归档操作中止。这个回调应该返回True使得操作继续。如果这个回调不存在，则归档操作继续进行
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
        return True

    def onRestore(self):
        '''
            如果这个函数在脚本中有实现，这个函数在Entity应用程序崩溃后在其它Entity应用程序上重新创建该实体时被调用。这个函数没有参数。
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
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
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))

        if userData == 0:
            # self.delTimer(timerHandle)
            self.lastSelCharacter += 1
            debug.DEBUG_MSG("change self.lastSelCharacter=====================")
        elif userData == 1:
            self.QQQQ.cccccc += 1
            debug.DEBUG_MSG("change self.QQQQ.cccccc=====================")

    def onTeleportFailure(self):
        '''
            如果这个函数在脚本中有实现，当用户调用Entity.teleport失败时该回调被调用


            def teleport( self, baseEntityMB ):

                teleport会瞬移这个实体的cell部分到参数指定的实体所在的空间。

                在抵达新的空间后，Entity.onTeleportSuccess被调用。这可以用来在新的空间里移动该实体到合适的位置。
                参数： baseEntityMB 实体应该移到的指定实体所在的空间，baseEntityMB即指定实体的EntityCall。
                当成功的时候，与此参数相关联的cell实体会被传入到Entity.onTeleportSuccess函数。
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
        pass

    def onTeleportSuccess(self, nearbyEntity):
        '''
            如果这个函数在脚本中有实现，当用户调用Entity.teleport成功时该回调被调用。
            参数：
                nearbyEntity  这个参数由用户调用 Entity.teleport时给出。这是一个real实体
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
        pass

    def onWriteToDB(self, cellData):
        '''
            如果这个函数在脚本中有实现，这个函数在实体数据将要写进数据库的时候被调用。

            需要注意的是在该回调里调用writeToDB会导致无限循环。
            参数：
                cellData 包含将要存进数据库的cell属性。 cellData是一个字典。
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
        pass

    '''
        proxy 事件回调
    '''

    def onClientDeath(self):
        '''
            如果在脚本中实现了此回调，这个方法将在客户端断开连接时被调用。 这个方法没有参数
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))

        # 有 cell 部分, 删除 cell, 在 cell 被删除的通知中再删除 self
        if self.cell:
            self.destroyCellEntity()
        else:
            self.destroy()

        pass

    def onClientGetCell(self):
        '''
            如果在脚本中实现了此回调，当客户端能够调用实体的cell属性时，该回调被调用
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
        pass

    def onClientEnabled(self):
        """
            kbe method.
            该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的cell部分。

            如果在脚本中实现了此回调，当实体可用时（ 各种初始化完毕并且可以与客户端通讯 ）该回调被调用。 这个方法没有参数。
            注意：giveClientTo将控制权赋给了该实体时也会导致该回调被调用
        """
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
        pass

    def onGiveClientToFailure(self):
        '''
            如果在脚本中实现了此回调，当实体调用giveClientTo失败时，该回调被调用。这个方法没有参数
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
        pass

    def onLogOnAttempt(self, ip, port, password):
        '''
            如果在脚本中实现了此回调，这个函数在客户端尝试使用当前账号实体进行登录时触发回调。
            这种情况通常是实体存在于内存中处于有效状态，最明显的例子是用户A使用此账号登录了，用户B使用同一账号进行登录，此时回调触发。

            这个回调函数可以返回如下常量值：
            kbe.LOG_ON_ACCEPT：允许新的客户端与实体进行绑定，如果实体已经绑定了一个客户端，之前的客户端将被踢出。
            kbe.LOG_ON_REJECT：拒绝新的客户端与实体绑定。
            kbe.LOG_ON_WAIT_FOR_DESTROY：等待实体销毁后再进行客户端绑定。


            参数：
                ip  尝试登录的客户端IP地址。
                port  尝试登录的客户端连接的端口。
                password  用户登录时使用的MD5密码。
        '''


        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))

        if self.avatarEntity:
            if self.avatarEntity.client:
                # giveClinetTo 必须是自身没有, 而目标有客户端连接
                # 是否这里会导致 baseapp 中 pEntity->clientEntityCall() 判断结果
                self.avatarEntity.giveClientTo(self)

            # 进入到 avatar 的清理逻辑
            self.avatarEntity.destroySelf()

            # 重置, 使得每次申请进入游戏时, avatarEntity 都是 None
            self.avatarEntity = None

            return kbe.LOG_ON_ACCEPT

    def onStreamComplete(self, id, success):
        '''
            如果在脚本中实现了此回调，当用户使用Proxy.streamStringToClient()或Proxy.streamFileToClient()完成时，该回调被调用。
            参数：
                id  与下载关联的id。
                success  成功与否。
        '''
        debug.DEBUG_MSG("%s-%s, dbID:%d, addr:%d" % (self.__class__.__name__, sys._getframe().f_code.co_name, self.id, id(self)))
        pass

    '''
        上面是事件回调
        下面是自定义函数
    '''

    def sayHelloOnBase(self, int_val, str_val, int_len):
        debug.DEBUG_MSG("sayHelloOnBase: %d-%s-%d" % (int_val, str_val, int_len))
        self.client.sayHelloOnClient(int_val * 2, str_val * 2, int_len * 2)

        self.change_test_val(int_val, str_val, int_len)

    def change_test_val(self, int_val, str_val, int_len):
        debug.DEBUG_MSG("change_test_val: %d-%s-%d" % (int_val, str_val, int_len))

        # 更改单个
        val = dict()
        val["param1"] = int_val
        val["param2"] = str_val

        self.test_val = val

        # 整体更新可以收到回调
        # 更改列表 
        # list_val = dict()
        # list_val["id"] = 1
        # list_val["name"] = "zhang san"
        # list_val["data"] = [val] * int_len

        # self.test_val_list = list_val

        # 
        self.test_val_list["id"] = 1
        self.test_val_list["name"] = "zhang san"
        self.test_val_list["data"] = [val] * int_len

    def reqAvatarListOnBase(self):
        '''
            请求角色列表
        '''
        self.client.reqAvatarListResultOnClient(self.characters)

    def reqCreateAvatarOnBase(self, role_type, name):
        '''
            请求创建角色
        '''

        props = {
            "name": name,
            "roleType": role_type,
            "level": 1,
            "direction": (0, 0, 0),
            "position": (0, 0, 0),
        }

        avatar = kbe.createEntityLocally('Avatar', props)
        if avatar:
            avatar.writeToDB(self._onAvatarSaved)

            debug.DEBUG_MSG("start to create avatar: role type:%d, name:%s" % (role_type, name))
        else:
            debug.DEBUG_MSG("create avatar faile: role type:%d, name:%s" % (role_type, name))

    def reqRemoveAvatarOnBase(self, db_id):
        '''
            请求删除角色
        '''

        count = 0
        for v in self.characters:
            if v["db_id"] == db_id:
                self.characters.remove(v)
                count += 1
                break

        self.client.reqRemoveAvatarResultOnClient(count)

    def selectAvatarEnterGameOnBase(self, db_id):
        '''
            申请进入游戏
        '''

        kbe.createEntityFromDBID("Avatar", db_id, self.__onAvatarCreated)

    def __onAvatarCreated(self, baseRef, dbid, wasActive):
        """
            选择角色进入游戏时被调用
        """
        if wasActive:
            debug.ERROR_MSG("Account::__onAvatarCreated:(%i): this character is in world now!" % (self.id))
            return
        if baseRef is None:
            debug.ERROR_MSG("Account::__onAvatarCreated:(%i): the character you wanted to created is not exist!" % (self.id))
            return

        avatar = kbe.entities.get(baseRef.id)
        if avatar is None:
            debug.ERROR_MSG("Account::__onAvatarCreated:(%i): when character was created, it died as well!" % (self.id))
            return

        if self.isDestroyed:
            debug.ERROR_MSG("Account::__onAvatarCreated:(%i): i dead, will the destroy of Avatar!" % (self.id))
            avatar.destroy()
            return

        self.avatarEntity = avatar
        avatar.setAccountEntity(self)

        self.giveClientTo(avatar)

    def _onAvatarSaved(self, success, avatar):
        """
            新建角色写入数据库回调
        """

        debug.DEBUG_MSG("_onAvatarSaved begin: %d" % success)

        # 如果此时账号已经销毁， 角色已经无法被记录则我们清除这个角色
        if self.isDestroyed:
            if avatar:
                avatar.destroy(True)

            return

        # 开始准备保存到 account 实体中
        avatarinfo = dict()

        if success:
            avatarinfo["db_id"] = avatar.databaseID
            avatarinfo["name"] = avatar.cellData["name"]
            avatarinfo["role_type"] = avatar.cellData["roleType"]
            avatarinfo["Level"] = avatar.cellData["level"]
            avatarinfo["Addr_Id"] = avatar.cellData["Addr_Id"]
            avatarinfo["Exp"] = 0

            self.characters.append(avatarinfo)
            self.lastSelCharacter = avatar.databaseID

            self.writeToDB()

        avatar.destroy()

        # 通知客户端
        if self.client:
            self.client.reqCreateAvatarResultOnClient(not success, avatarinfo)

    def createAvatar(self):

        if self.lastSelCharacter == 0:
            def onCreateEntityCallback(entity):
                if entity:
                    self.avatarEntity = entity

                debug.WARNING_MSG("createAvatar={}".format(entity))

            kbe.createEntityAnywhere("Avatar", {}, onCreateEntityCallback)
        else:
            def onCreateEntityCallback(baseRef, databaseID, wasActive):
                if baseRef:
                    self.avatarEntity = baseRef

            kbe.createEntityAnywhereFromDBID("Avatar", self.lastSelCharacter, onCreateEntityCallback)

    def giveClientToAvatar(self):
        self.giveClientTo(self.avatarEntity)