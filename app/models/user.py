from app.common.json_encoder import JSONSerializable

class User(JSONSerializable):
    def __init__(self, name):
        self.name = name

    def toJSON(self):
        return self.__dict__