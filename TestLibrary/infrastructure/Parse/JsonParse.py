import json

class JsonParse(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass

    @staticmethod
    def content_to_json(content):
        return json.loads(content)

    @staticmethod
    def get_from_json(jsonobj, key):
        return  jsonobj[key]
