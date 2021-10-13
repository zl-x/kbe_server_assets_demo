# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class Entity_CallBack_Record(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)

    def onDestroy(self):
        '''
            如果这个函数在脚本中有实现，这个函数在调用Entity.destroy()后，在实际销毁之前被调用。这个函数没有参数
        '''
        pass

    def onEnterTrap(self, entity, rangeXZ, rangeY, controllerID, userArg):
        '''
            当注册了使用Entity.addProximity注册了一个范围触发器，有其他实体进入触发器时，该回调函数被调用。

            参数：
                entity  已经进入了范围的实体。

                rangeXZ float，给定触发器xz轴区域的大小，必须大于等于0。

                rangeY float，给定触发器y轴高度，必须大于等于0。
                需要注意的是，这个参数要生效必须开放kbengine_defaults.xml->cellapp->coordinate_system->rangemgr_y
                开放y轴管理会带来一些消耗，因为一些游戏大量的实体都在同一y轴高度或者在差不多水平线高度，此时碰撞变得非常密集。
                3D太空类游戏或者小房间类实体较少的游戏比较适合开放此选项。

                controllerID  这个触发器的控制器id。
                userArg  这个参数的值由用户调用addProximity时给出，用户可以根据此参数对当前行为做一些判断。
        '''
        pass

    def onEnteredView(self, entity):
        '''
            如果这个函数在脚本中有实现，当一个实体进入了当前实体的View范围，该回调被触发。
            参数：
                entity  进入View范围的实体。
        '''
        pass

    def onGetWitness(self):
        '''
            如果这个函数在脚本中有实现，当实体绑定了Witness时被调用。
            也可以访问实体属性Entity.hasWitness得到实体当前的状态。
        '''
        pass

    def onLeaveTrap(self, entity, rangeXZ, rangeY, controllerID, userArg):
        '''
            如果这个函数在脚本中有实现，当实体离开了当前实体注册的范围触发器区域时被触发，范围触发器由Entity.addProximity注册。
            参数：
                entity  已经离开触发器区域的实体。
                rangeXZ float，给定触发器xz轴区域的大小，必须大于等于0。
                rangeY float，给定触发器y轴高度，必须大于等于0。
                需要注意的是，这个参数要生效必须开放kbengine_defaults.xml->cellapp->coordinate_system->rangemgr_y
                开放y轴管理会带来一些消耗，因为一些游戏大量的实体都在同一y轴高度或者在差不多水平线高度，此时碰撞变得非常密集。
                3D太空类游戏或者小房间类实体较少的游戏比较适合开放此选项。
                controllerID  这个触发器的控制器ID。
                userArg  这个参数的值由用户调用addProximity时给出，用户可以根据此参数对当前行为做一些判断。
        '''
        pass

    def onLoseControlledBy(self, id):
        '''
            如果这个函数在脚本中有实现，当Entity.controlledBy 所关联的实体丢失时改回调方法被调用。

            参数：
                id  controlledBy实体的ID。
        '''
        pass

    def onLoseWitness(self):
        '''
            如果这个函数在脚本中有实现，当实体解除Witness时，该回调被触发。
            也可以访问实体属性Entity.hasWitness得到实体当前的状态。
        '''
        pass

    def onMove(self, controllerID, userData):
        '''
            如果这个函数在脚本中有实现，相关的Entity.moveToPoint与Entity.moveToEntity还有Entity.navigate方法被调用并且成功后底层每帧移动都会回调此函数。

            参数：
                controllerID  与某个移动相关的控制器ID。
                userData  这个参数值由用户在请求移动相关接口时给出。
        '''
        pass

    def onMoveOver(self, controllerID, userData):
        '''
            如果这个函数在脚本中有实现，相关的Entity.moveToPoint与Entity.moveToEntity还有Entity.navigate方法被调用后到达指定目标点时会回调此函数。

            参数：
                controllerID  与某个移动相关的控制器ID。
                userData  这个参数值由用户在请求移动相关接口时给出。
        '''
        pass

    def onMoveFailure(self, controllerID, userData):
        '''
            如果这个函数在脚本中有实现，相关的Entity.moveToPoint与Entity.moveToEntity还有Entity.navigate方法被调用并且失败时会回调此函数。

            参数：
                controllerID  与某个移动相关的控制器ID。
                userData  这个参数值由用户在请求移动相关接口时给出。
        '''
        pass

    def onRestore(self):
        '''
            如果这个函数在脚本中有实现，这个函数在Cell应用程序崩溃后在其它Cell应用程序上重新创建该实体时被调用。这个函数没有参数。
        '''
        pass

    def onSpaceGone(self):
        '''
            如果这个函数在脚本中有实现，当前实体所在的Space将要销毁时触发 。这个函数没有参数。
        '''
        pass

    def onTurn(self, controllerID, userData):
        '''
            如果这个函数在脚本中有实现，相关的Entity.addYawRotator方法被调用后到达指定yaw时会回调此函数。

            参数：
                controllerID  Entity.addYawRotator返回的控制器ID。
                userData  这个参数值由用户在请求移动相关接口时给出。
        '''
        pass

    def onTeleport(self):
        '''
            如果这个函数在脚本中有实现，在通过baseapp的Entity.teleport调用发生的实体传送中，实体(Real entity)被传送之前的时刻此方法会被调用。
            请注意，在cell上调用实体的teleport并不会回调此接口，如果你需要这个功能请在Entity.teleport之后调用此回调。
        '''
        pass

    def onTeleportFailure(self):
        '''
            如果这个函数在脚本中有实现，当用户调用Entity.teleport失败时该回调被调用。
        '''
        pass

    def onTeleportSuccess(self, nearbyEntity):
        '''
            如果这个函数在脚本中有实现，当用户调用Entity.teleport成功时该回调被调用。
            参数：
                nearbyEntity  这个参数由用户调用 Entity.teleport时给出。这是一个real实体。
        '''
        pass

    def onTimer(self, timerHandle, userData):
        '''
            这个函数当一个与此实体关联的定时器触发的时候被调用。一个定时器可以使用Entity.addTimer函数添加。
            参数：
                timerHandle 定时器的id。
                userData 传进Entity.addTimer的integer用户数据。
        '''
        pass

    def onUpdateBegin(self):
        '''
            当同步一帧开始时被调用。
        '''
        pass

    def onUpdateEnd(self):
        '''
            当同步一帧结束时被调用。
        '''
        pass

    def onWitnessed(self, isWitnessed):
        '''
            如果这个函数在脚本中有实现，如果当前实体进入了另一个绑定了Witness的实体的View范围（也可以理解为一个实体被观察者观察到了），则该实体的回调函数被调用。
            可以利用这个函数在实体被观察时激活实体的AI，实体停止被观察时可以停止AI的执行，这样可以降低服务端的计算量从而提升效率。

            参数：
                isWitnessed  bool，实体被观察时为True，实体被停止观察时是False。
                也可以访问实体属性Entity.isWitnessed得到实体当前的状态
        '''
        pass

    def onWriteToDB(self):
        '''
            如果这个函数在脚本中有实现，这个函数在实体将要存档到数据库时被调用。
        '''
        pass