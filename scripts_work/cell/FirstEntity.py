# -*- coding: utf-8 -*-
import kbengine.cell as kbe
from kbengine import debug


class FirstEntity(kbe.Entity):
    """
    第一个实体的cell部分的实现
    """

    def __init__(self):
        kbe.Entity.__init__(self)
        # 通知客户端，本实体已进入
        self.client.onEnter()

    def say(self, callerID, content):
        """
        实现了CellMethods中的say方法，content即为申明的类型为UNICODE的参数
        :param callerID: 调用者ID
        :param content: say的内容
        :return:
        """
        debug.INFO_MSG("FirstEntity::say")
        # 广播给所有客户端的onSay方法
        self.allClients.onSay("Entity: " + str(self.id) + " " + content)
