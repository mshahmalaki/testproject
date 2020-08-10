from flask import request, abort
from auth import db
from auth.model import User
from auth.schema import UserSchema


class UserController:
    def get_users():
        users = User.query.all()
        users_schema = UserSchema(many=True)
        return {"users": users_schema.dump(users)}

    def get_user(user_id):
        user = User.query.get(user_id)
        if user is None:
            abort(404)
        user_schema = UserSchema()
        return {"user": user_schema.dump(user)}

    def create_user():
        json_data = request.get_json()
        user_schema = UserSchema()
        try:
            data = user_schema.load(json_data)
        except:
            abort(400)
        user = User.query.filter_by(username=data["username"]).first()
        if user is None:
            user = User(
                username=data["username"],
                password=data["password"],
                address=data["address"],
            )
            db.session.add(user)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                abort(500)
            return {"user": user_schema.dump(user)}, 201
        else:
            abort(409)

    def update_user(user_id):
        json_data = request.get_json()
        user_schema = UserSchema()
        try:
            data = user_schema.load(json_data)
        except:
            abort(400)
        user = User.query.get(user_id)
        if user is None:
            abort(404)
        else:
            user.username = data["username"]
            user.password = data["password"]
            user.address = data["address"]
            try:
                db.session.commit()
            except:
                db.session.rollback()
                abort(500)
            return {"message": "A Specific User Updated"}, 204

    def delete_user(user_id):
        user = User.query.get(user_id)
        if user is None:
            abort(404)
        db.session.delete(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500)
        return {"message": "A Specific User Deleted"}, 204
