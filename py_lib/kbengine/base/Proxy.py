from . import Entity


class Proxy(Entity.Entity):
    __ACCOUNT_NAME__ = None
    __ACCOUNT_PASSWORD__ = None
    clientAddr = None
    clientEnabled = None
    hasClient = None
    roundTripTime = None
    timeSinceHeardFromClient = None

    def disconnect(self):
        super(Proxy, self).disconnect()

    def getClientType(self):
        super(Proxy, self).getClientType()

    def getClientDatas(self):
        super(Proxy, self).getClientDatas()

    def giveClientTo(self, proxy):
        super(Proxy, self).giveClientTo(proxy)

    def streamFileToClient(self, resourceName, desc="", id=-1):
        super(Proxy, self).streamFileToClient(resourceName, desc, id)

    def streamStringToClient(self, data, desc="", id=-1):
        super(Proxy, self).streamStringToClient(data, desc, id)

    def onClientDeath(self):
        super(Proxy, self).onClientDeath()

    def onClientGetCell(self):
        super(Proxy, self).onClientGetCell()

    def onClientEnabled(self):
        super(Proxy, self).onClientEnabled()

    def onGiveClientToFailure(self):
        super(Proxy, self).onGiveClientToFailure()

    def onLogOnAttempt(self, ip, port, password):
        super(Proxy, self).onLogOnAttempt(ip, port, password)

    def onStreamComplete(self, id, success):
        super(Proxy, self).onStreamComplete(id, success)

