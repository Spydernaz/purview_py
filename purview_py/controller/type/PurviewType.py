from purview_py.controller.type.Attribute import PurviewAttribute, PurviewRelationshipAttribute
from datetime import datetime
import requests, json, uuid


class PurviewType(object):
    
    def __init__(self, category, name, serviceType, superTypes, subTypes=[], guid=str(uuid.uuid4()), createdBy="purview_py", updatedBy="purview_py", createTime=datetime.now(), updateTime=datetime.now(), version=2, description="", typeVersion="1.0", options={}, lastModifiedTS=None, attributeDefs=[], relationshipAttributeDefs=[], newType=False):
        self.category = category
        self.createdBy = createdBy
        self.updatedBy = updatedBy
        self.createTime = createTime
        self.updateTime = updateTime
        self.version = version
        self.name = name
        self.description = description
        self.typeVersion = typeVersion
        self.serviceType = serviceType
        self.options = options
        self.lastModifiedTS = lastModifiedTS
        self.attributeDefs = attributeDefs
        self.superTypes = superTypes
        self.subTypes = subTypes
        self.relationshipAttributeDefs = relationshipAttributeDefs
        self.newType = newType

    @classmethod
    def getTypeByName(cls, conn, name):
        urlheaders = {"Content-Type": "application/json", "Authorization": f"Bearer {conn.auth.getToken()}"}
        response = requests.get(f"{conn.purviewEndpoint}/catalog/api/atlas/v2/types/typedef/name/{name}", headers=urlheaders)
        if response.status_code == 200:
            return cls.getClassByJSON(response.json())
        else:
            raise Exception(response.status_code, response.json())

    @classmethod
    def getTypeByGUID(cls, guid, conn):
        urlheaders = {"Content-Type": "application/json", "Authorization": f"Bearer {conn.auth.getToken()}"}
        response = requests.get(f"{conn.purviewEndpoint}/catalog/api/atlas/v2/types/typedef/guid/{guid}", headers=urlheaders)
        if response.status_code == 200:
            return cls.getClassByJSON(response.json())
        else:
            raise Exception(response.status_code, response.json())

    @classmethod
    def getClassByJSON(cls, apiresp):
        args = dict(apiresp)
        tmpAttributes = []
        tmpRelAttributes = []

        for attr in args["attributeDefs"]:
            tmpAttributes.append(PurviewAttribute(*attr))
        for attr in args["relationshipAttributeDefs"]:
            tmpRelAttributes.append(PurviewRelationshipAttribute(*attr))

        args["attributeDefs"] = tmpAttributes
        args["relationshipAttributeDefs"] = tmpRelAttributes

        t = cls(*args, newType=False)
        return t

        