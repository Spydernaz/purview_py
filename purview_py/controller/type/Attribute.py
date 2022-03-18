

class PurviewRelationshipAttribute(object):

    def __init__(self, name, typeName, relationshipTypeName, cardinality, valuesMinCount, valuesMaxCount, constraints=[], isOptional=True, isUnique=False, isIndexable=False, includeInNotification=False, isLegacyAttribute=False):
        self.name = name
        self.typeName = typeName
        self.relationshipTypeName = relationshipTypeName
        self.cardinality = cardinality
        self.valuesMinCount = valuesMinCount
        self.valuesMaxCount = valuesMaxCount
        self.isOptional = isOptional
        self.isUnique = isUnique
        self.isIndexable = isIndexable
        self.includeInNotification = includeInNotification
        self.isLegacyAttribute = isLegacyAttribute

class PurviewAttribute(object):

    def __init__(self, name, typename, cardinality, valuesMinCount, valuesMaxCount, isOptional=True, isUnique=False, isIndexable=False, includeInNotification=False):
        self.name = name
        self.typename = typename
        self.cardinality = cardinality
        self.valuesMinCount = valuesMinCount
        self.valuesMaxCount = valuesMaxCount
        self.isOptional = isOptional
        self.isUnique = isUnique
        self.isIndexable = isIndexable
        self.includeInNotification = includeInNotification