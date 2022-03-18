from purview_py.controller.type import PurviewType
from purview_py.controller.entity import PurviewEntity
from purview_py.conn import Connection

class PurviewController(object):
    """A controller for Purview"""

    def __init__(self, conn):
        self.conn = conn
        self.purviewEndpoint = f"https://{self.resource}.purview.azure.com"

    def getTypeByName(self, name):
        return PurviewType.getTypeByName(name, auth)