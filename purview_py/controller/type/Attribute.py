
class AttributeDef(object):
    def __init__(self):
        pass

class PurviewRelationshipAttributeDef(AttributeDef):

    def __init__(self, name, typeName, relationshipTypeName, cardinality, valuesMinCount, valuesMaxCount, constraints=[], isOptional=True, isUnique=False, isIndexable=False, includeInNotification=False, isLegacyAttribute=False):
        self.name = str(name)
        self.typeName = str(typeName)
        self.relationshipTypeName = str(relationshipTypeName)
        self.cardinality = str(cardinality)
        self.valuesMinCount = int(valuesMinCount)
        self.valuesMaxCount = int(valuesMaxCount)
        self.isOptional = bool(isOptional)
        self.isUnique = bool(isUnique)
        self.isIndexable = bool(isIndexable)
        self.includeInNotification = bool(includeInNotification)
        self.isLegacyAttribute = bool(isLegacyAttribute)
    

class PurviewAttributeDef(AttributeDef):

    def __init__(self, name, typeName, cardinality, valuesMinCount, valuesMaxCount, isOptional=True, isUnique=False, isIndexable=False, includeInNotification=False, isLegacyAttribute=False):
        self.name = str(name)
        self.typeName = str(typeName)
        self.cardinality = str(cardinality)
        self.valuesMinCount = int(valuesMinCount)
        self.valuesMaxCount = int(valuesMaxCount)
        self.isOptional = bool(isOptional)
        self.isUnique = bool(isUnique)
        self.isIndexable = bool(isIndexable)
        self.includeInNotification = bool(includeInNotification)
        self.isLegacyAttribute = bool(isLegacyAttribute)
