from flask import Flask, request, jsonify, json

# Init app
app = Flask(__name__)

# Make Flask App uses custom JSON Encoder
class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            # this returns dictionary (which is serializable)
            return obj.__dict__
        return super(MyJSONEncoder, self).default(obj)

app.json_encoder = MyJSONEncoder

# Routes
@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello World"})

@app.route("/users", methods=["POST"])
def create_user():
    name = request.json["name"]
    new_user = User(name)
    users.append(new_user)
    return jsonify({"message": "OK"})

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Models
class User(json.JSONEncoder):
    def __init__(self, name):
        self.name = name

# Data
users = [User("Hung")]

# Run server
if __name__ == "__main__":
    app.run(debug=True)