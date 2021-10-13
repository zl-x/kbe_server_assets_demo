import KBEngine


class Entity(KBEngine.Entity):
    cell = None
    cellData = None
    className = None
    client = None
    databaseID = None
    databaseInterfaceName = None
    id = None
    isDestroyed = None
    shouldAutoArchive = None
    shouldAutoBackup = None

    def addTimer(self, initialOffset, repeatOffset=0, userArg=0):
        super(Entity, self).addTimer(initialOffset, repeatOffset, userArg)

    def createCellEntity(self, cellEntityCall):
        super(Entity, self).createCellEntity(cellEntityCall)

    def createCellEntityInNewSpace(self, cellappIndex):
        super(Entity, self).createCellEntityInNewSpace(cellappIndex)

    def delTimer(self, id):
        super(Entity, self).delTimer(id)

    def destroy(self, deleteFromDB, writeToDB):
        super(Entity, self).destroy(deleteFromDB, writeToDB)

    def destroyCellEntity(self):
        super(Entity, self).destroyCellEntity()

    def getComponent(self, componentName, all):
        super(Entity, self).getComponent(componentName, all)

    def fireEvent(self, eventName, *args):
        super(Entity, self).fireEvent(eventName, *args)

    def registerEvent(self, eventName, callback):
        super(Entity, self).registerEvent(eventName, callback)

    def deregisterEvent(self, eventName, callback):
        super(Entity, self).deregisterEvent(eventName, callback)

    def writeToDB(self, callback, shouldAutoLoad, dbInterfaceName):
        super(Entity, self).writeToDB(callback, shouldAutoLoad, dbInterfaceName)

    def onCreateCellFailure(self):
        super(Entity, self).onCreateCellFailure()

    def onDestroy(self):
        super(Entity, self).onDestroy()

    def onGetCell(self):
        super(Entity, self).onGetCell()

    def onLoseCell(self):
        super(Entity, self).onLoseCell()

    def onPreArchive(self):
        super(Entity, self).onPreArchive()

    def onRestore(self):
        super(Entity, self).onRestore()

    def onTimer(self, timerHandle, userData):
        super(Entity, self).onTimer(timerHandle, userData)

    def onWriteToDB(self, cellData):
        super(Entity, self).onWriteToDB(cellData)
