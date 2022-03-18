

class PurviewType(object):
    
    def __init__(self, args, newType=False):

        self.category
        self.guid # generate or get
        self.createdBy
        self.updatedBy
        self.createTime
        self.updateTime
        self.version
        self.name
        self.description
        self.typeVersion
        self.serviceType
        self.options
        self.lastModifiedTS
        self.attributeDefs
        self.superTypes
        self.subTypes
        self.relationshipAttributeDefs

    @classmethod
    def getTypeByName(cls, name):
        pass

    @classmethod
    def getTypeByGUID(cls, guid):
        pass

    @classmethod
    def getClassByJSON(cls, json):
        pass