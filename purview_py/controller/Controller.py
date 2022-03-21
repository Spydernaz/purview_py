# from purview_py import PurviewType, PurviewEntity, Connection
import pprint, requests


class PurviewController(object):
    """A controller for Purview"""

    def __init__(self):
        pass

    def createNewTypes(self, conn, types):
        # Check manditory fields
        # format request
        # post data
        #check response code
        if type(types) != list:
            types = [types]

        requestdata = {"entityDefs":[], "classificationDefs":[], "structDefs":[], "relationshipDefs":[]}
        # pp = pprint.PrettyPrinter(indent=4)
        
        for t in types:
            type_dict = t.format_for_requests()
            type_dict.pop('guid', None)

            if type_dict["category"] == "ENTITY":
                requestdata["entityDefs"].append(type_dict)
            if type_dict["category"] == "CLASSIFICATION":
                requestdata["classificationDefs"].append(type_dict)
            if type_dict["category"] == "STRUCT":
                requestdata["structDefs"].append(type_dict)
            if type_dict["category"] == "RELATIONSHIP":
                requestdata["relationshipDefs"].append(type_dict)

        # Format Request
        r = requests.post(f"{conn.purviewEndpoint}/catalog/api/atlas/v2/types/typedefs", headers=conn.headers, json=requestdata)

        if r.status_code != 200:
            return f"{r.status_code}: {r.json()}"
        else:
            return r.status_code

    def updateExistingTypes(self, conn, types):
        # Check manditory fields
        # format request
        # post data
        #check response code
        if type(types) != list:
            types = [types]

        requestdata = {"entityDefs":[], "classificationDefs":[], "structDefs":[], "relationshipDefs":[]}
        # pp = pprint.PrettyPrinter(indent=4)
        
        for t in types:
            type_dict = t.format_for_requests()
            type_dict.pop('guid', None)

            if type_dict["category"] == "ENTITY":
                requestdata["entityDefs"].append(type_dict)
            if type_dict["category"] == "CLASSIFICATION":
                requestdata["classificationDefs"].append(type_dict)
            if type_dict["category"] == "STRUCT":
                requestdata["structDefs"].append(type_dict)
            if type_dict["category"] == "RELATIONSHIP":
                requestdata["relationshipDefs"].append(type_dict)

        # Format Request
        r = requests.put(f"{conn.purviewEndpoint}/catalog/api/atlas/v2/types/typedefs", headers=conn.headers, json=requestdata)

        if r.status_code != 200:
            return f"{r.status_code}: {r.json()}"
        else:
            return r.status_code


