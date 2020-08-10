from flask_restx import Resource
from flask import abort
from auth.controller import UserController


class UserResource(Resource):
    def get(self, user_id=None):
        if user_id is None:
            print("Collection Called")
            return UserController.get_users()
        else:
            print("Singleton Called")
            return UserController.get_user(user_id)

    def post(self, user_id=None):
        if user_id is None:
            print("Create User")
            return UserController.create_user()
        else:
            abort(405)

    def put(self, user_id=None):
        if user_id is None:
            abort(405)
        else:
            print("Update Specific User")
            return UserController.update_user(user_id)

    def delete(self, user_id=None):
        if user_id is None:
            abort(405)
        else:
            print("The Specific User is Deleted")
            return UserController.delete_user(user_id)
