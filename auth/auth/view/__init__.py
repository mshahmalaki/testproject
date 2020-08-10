from auth import api
from auth.view.users import UserResource


api.add_resource(UserResource, "/users", methods=["GET", "POST", "PUT", "DELETE"], endpoint="users")
api.add_resource(UserResource, "/users/<int:user_id>", methods=["GET", "POST", "PUT", "DELETE"], endpoint="user")
