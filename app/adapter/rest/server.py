from flask import Flask, request, jsonify
from app.models.user import User
from app.common.json_encoder import MyJSONEncoder
from app.services.repo.user_repo import UserRepoInterface
from app.services.user_service import UserService


class RestServer:
    app = Flask(__name__)
    user_service = UserService(UserRepoInterface())

    def __init__(self, user_repo):
        if not isinstance(user_repo, UserRepoInterface):
            raise ValueError("expected subclass of UserRepoInterface")
        
        self.user_service = UserService(user_repo)
        self.setup_json_encoder()
        self.setup_routes()

    def setup_json_encoder(self):
        self.app.json_encoder = MyJSONEncoder

    def setup_routes(self):
        @self.app.route("/users", methods=["POST"])
        @wrap_error
        def create_user():
            name = request.json["name"]
            new_user = User(name)
            self.user_service.create_user(new_user)
            return jsonify({"message": "OK"})

        @self.app.route("/users", methods=["GET"])
        @wrap_error
        def get_users():
            users = self.user_service.get_all()
            response = jsonify(users)
            response.status_code = 200
            return response

    def run(self):
        self.app.run(debug=True)


def wrap_error(f):
    def wrapper():
        try:
            result = f()
            return result
        except Exception as e:
            return jsonify({ "error": str(e) })

    wrapper.__name__ = f.__name__
    return wrapper