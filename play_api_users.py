from flask import Flask

# abstract
from api.api_users import AuthAPI, UserAPI, UserReadAPI
from component_interface.persitent import ReadOnlyIUserStorage
# model
from api.api_models import User
# concrete implementations
from component_db.sqlite_storage import UserStorageDict, JwtStorageDict
# flask view
from flask_view import auth_api_view


# jwt_storage
jwt_store = JwtStorageDict()
# user_storage
user_storage = UserStorageDict()
user_storage_read_only = ReadOnlyIUserStorage(user_storage)
# api_auth

user1 = User(user_id='user1', user_password='user1_pass')
user2 = User(user_id='user2', user_password='user2_pass')

user_storage.create(user1)
user_storage.create(user2)

auth = AuthAPI(user_store=user_storage_read_only,
               jwt_store=jwt_store)

# really simple testing

jwt_st1 = auth.authenticate('user1', 'user1_pass')
assert auth.is_authenticated(jwt_st1)
auth.revoke('user1', 'user1_pass', jwt_st1)
assert not auth.is_authenticated(jwt_st1)
jwt_st2 = auth.authenticate('user2', 'user2_pass')
assert auth.is_authenticated(jwt_st2)
js3 = auth.authenticate('user3', 'user3_pass')
assert not js3

# flask
app = Flask(__name__)
view = auth_api_view.AuthView(app=app, auth_api=auth)
app.run()
