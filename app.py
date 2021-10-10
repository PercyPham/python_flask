from app.adapter.memdb.user_repo import UserRepo
from app.adapter.rest.server import RestServer

user_repo = UserRepo()
server = RestServer(user_repo)

server.run()
