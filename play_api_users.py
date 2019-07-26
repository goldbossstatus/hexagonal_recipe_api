# abstract
from api.api_users import AuthAPI, UserAPI, UserReadAPI
from component_interface.persitent import ReadOnlyIUserStorage
# model
from api.api_models import User
# concrete implementations
from component_db.sqlite_storage import UserStorageDict, JwtStorageDict

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

# connect UserStorageSQLite to user api

#api = UserAPI(UserStorageSQLite(), 'key')

#print(api.read('user_id', api_key='key'))


