from purview_py.controller.type import PurviewType
from purview_py.controller.entity import PurviewEntity

class PurviewController(object):
    """A controller for Purview"""

    def __init__(self, resource, authToken):
        self.resource = resource
        self.authToken = authToken

        self.purviewEndpoint = f"https://{self.resource}.purview.azure.com"

    def getTypeByName(self, name):
        return PurviewType.getTypeByName(name, auth)