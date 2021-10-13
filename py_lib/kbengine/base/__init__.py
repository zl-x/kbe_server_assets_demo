import KBEngine

from kbengine.base.Entity import Entity
from kbengine.base.Proxy import Proxy

'''
    成员函数
'''


def addWatcher(path, dataType, getFunction):
    KBEngine.addWatcher(path, dataType, getFunction)


def address():
    KBEngine.address()


def MemoryStream():
    KBEngine.MemoryStream()


def charge(ordersID, dbID, byteDatas, pycallback):
    KBEngine.charge(ordersID, dbID, byteDatas, pycallback)


def createEntity():
    KBEngine.createEntity()


def createEntityAnywhere(entityType, *params, callback):
    KBEngine.createEntityAnywhere(entityType, *params, callback)


def createEntityRemotely(entityType, baseMB, *params, callback):
    KBEngine.createEntityRemotely(entityType, baseMB, *params, callback)


def createEntityFromDBID(entityType, dbID, callback, dbInterfaceName):
    KBEngine.createEntityFromDBID(entityType, dbID, callback, dbInterfaceName)


def createEntityAnywhereFromDBID(entityType, dbID, callback, dbInterfaceName):
    KBEngine.createEntityAnywhereFromDBID(entityType, dbID, callback, dbInterfaceName)


def createEntityRemotelyFromDBID(entityType, dbID, baseMB, callback, dbInterfaceName):
    KBEngine.createEntityRemotelyFromDBID(entityType, dbID, baseMB, callback, dbInterfaceName)


def createEntityLocally(entityType, *params):
    KBEngine.createEntityLocally(entityType, *params)


def debugTracing():
    KBEngine.debugTracing()


def delWatcher(path):
    KBEngine.delWatcher(path)


def deleteEntityByDBID(entityType, dbID, callback, dbInterfaceName):
    KBEngine.deleteEntityByDBID(entityType, dbID, callback, dbInterfaceName)


def deregisterReadFileDescriptor(fileDescriptor):
    KBEngine.deregisterReadFileDescriptor(fileDescriptor)


def deregisterWriteFileDescriptor(fileDescriptor):
    KBEngine.deregisterWriteFileDescriptor(fileDescriptor)


def executeRawDatabaseCommand(command, callback, threadID, dbInterfaceName):
    KBEngine.executeRawDatabaseCommand(command, callback, threadID, dbInterfaceName)


def genUUID64():
    KBEngine.genUUID64()


def getResFullPath(res):
    KBEngine.getResFullPath(res)


def getWatcher(path):
    KBEngine.getWatcher(path)


def getWatcherDir(path):
    KBEngine.getWatcherDir(path)


def getAppFlags():
    KBEngine.getAppFlags()


def hasRes(res):
    KBEngine.hasRes(res)


def isShuttingDown():
    KBEngine.isShuttingDown()


def listPathRes(path, extension):
    KBEngine.listPathRes(path, extension)


def lookUpEntityByDBID(entityType, dbID, callback, dbInterfaceName):
    KBEngine.lookUpEntityByDBID(entityType, dbID, callback, dbInterfaceName)


def matchPath(res):
    KBEngine.matchPath(res)


def open(res, mode, encoding):
    KBEngine.open(res, mode, encoding)


def publish():
    KBEngine.publish()


def quantumPassedPercent():
    KBEngine.quantumPassedPercent()


def registerReadFileDescriptor(fileDescriptor, callback):
    KBEngine.registerReadFileDescriptor(fileDescriptor, callback)


def registerWriteFileDescriptor(fileDescriptor, callback):
    KBEngine.registerWriteFileDescriptor(fileDescriptor, callback)


def reloadScript(fullReload):
    KBEngine.reloadScript(fullReload)


def scriptLogType(logType):
    KBEngine.scriptLogType(logType)


def setAppFlags(flags):
    KBEngine.setAppFlags(flags)


def time():
    KBEngine.time()


def urlopen(url, callback, postData, headers):
    KBEngine.urlopen(url, callback, postData, headers)


'''
    回调函数
'''


def onBaseAppReady(isBootstrap):
    KBEngine.onBaseAppReady(isBootstrap)


def onBaseAppShutDown(state):
    KBEngine.onBaseAppShutDown(state)


def onCellAppDeath(addr):
    KBEngine.onCellAppDeath(addr)


def onFini():
    KBEngine.onFini()


def onBaseAppData(key, value):
    KBEngine.onBaseAppData(key, value)


def onBaseAppDataDel(key):
    KBEngine.onBaseAppDataDel(key)


def onGlobalData(key, value):
    KBEngine.onGlobalData(key, value)


def onGlobalDataDel(key):
    KBEngine.onGlobalDataDel(key)


def onInit(isReload):
    KBEngine.onInit(isReload)


def onLoseChargeCB(orderID, dbID, success, datas):
    KBEngine.onLoseChargeCB(orderID, dbID, success, datas)


def onReadyForLogin(isBootstrap):
    KBEngine.onReadyForLogin(isBootstrap)


def onReadyForShutDown():
    KBEngine.onReadyForShutDown()


def onAutoLoadEntityCreate(entityType, dbID):
    KBEngine.onAutoLoadEntityCreate(entityType, dbID)


'''
    属性
'''
LOG_ON_ACCEPT = KBEngine.LOG_ON_ACCEPT
LOG_ON_REJECT = KBEngine.LOG_ON_REJECT
LOG_ON_WAIT_FOR_DESTROY = KBEngine.LOG_ON_WAIT_FOR_DESTROY
LOG_TYPE_DBG = KBEngine.LOG_TYPE_DBG
LOG_TYPE_ERR = KBEngine.LOG_TYPE_ERR
LOG_TYPE_INFO = KBEngine.LOG_TYPE_INFO
LOG_TYPE_NORMAL = KBEngine.LOG_TYPE_NORMAL
LOG_TYPE_WAR = KBEngine.LOG_TYPE_WAR
NEXT_ONLY = KBEngine.NEXT_ONLY
component = KBEngine.component
entities = KBEngine.entities
baseAppData = KBEngine.baseAppData
globalData = KBEngine.globalData
