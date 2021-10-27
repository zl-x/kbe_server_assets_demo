# -*- coding: utf-8 -*-
import kbengine.base as kbe
from kbengine import debug

from base import Avatar


class Account(kbe.Proxy):
    roleIdList = list()

    def __init__(self):
        kbe.Proxy.__init__(self)
        self.activeAvatar: Avatar.Avatar = None
        self.avatarId2Entity = dict()

    def onClientEnabled(self):
        """
            kbe method.
            该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的cell部分。

            如果在脚本中实现了此回调，当实体可用时（ 各种初始化完毕并且可以与客户端通讯 ）该回调被调用。 这个方法没有参数。
            注意：giveClientTo将控制权赋给了该实体时也会导致该回调被调用
        """

        debug.ERROR_MSG("avatar dbid list={}".format(self.roleIdList))

        def cb(baseRef: Avatar.Avatar, databaseID: int, wasActive: bool):
            if not baseRef:
                debug.ERROR_MSG("create avatar dbid={} active={}".format(databaseID, wasActive))
                return

            debug.DEBUG_MSG("create avatar dbid={} active={}".format(databaseID, wasActive))

            self.avatarId2Entity[databaseID] = baseRef

        for dbId in self.roleIdList:
            kbe.createEntityAnywhereFromDBID("Avatar", dbId, cb)

    def onDestroy(self):
        debug.ERROR_MSG("account onDestroy")

    def onLogOnAttempt(self, ip, port, password):
        if self.activeAvatar and self.activeAvatar.hasClient:
            self.activeAvatar.OnReplaceLogin()

        return kbe.LOG_ON_ACCEPT

    def giveClinetToAccountEntity(self):
        '''
            转让客户端发送消息到 base 的 entity 的权限
        '''
        if not self.avatarId2Entity:
            debug.ERROR_MSG("self.avatarId2Entity emtpy")
            return

        firstKey = list(self.avatarId2Entity.keys())[-1]
        self.activeAvatar: Avatar.Avatar = self.avatarId2Entity[firstKey]

        self.activeAvatar.setAccountEntity(self)
        self.giveClientTo(self.activeAvatar)

    def sayHello(self, arg1: int, arg2: str, arg3: int) -> None:
        pass

    def reqAvatarList(self):
        pass

    def reqCreateAvatar(self, arg1: int, arg2: str) -> None:
        param = dict(
            name=arg2,
            roleType=arg1,
        )

        def cb(avatarEntity: Avatar.Avatar):
            debug.ERROR_MSG("avatar created{}".format(avatarEntity))
            if not avatarEntity:
                return

        kbe.createEntityAnywhere("Avatar", param, cb)

    def reqRemoveAvatar(self, arg1: int) -> None:
        pass

    def selectAvatarEnterGame(self, arg1: int) -> None:
        pass
