from json import JSONEncoder

class JSONSerializable:
    def toJSON(self):
        '''
        This method requires to return a dictionary (since it's JSON serializable)
        '''
        pass

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JSONSerializable):
            return obj.toJSON()
        return super(MyJSONEncoder, self).default(obj)