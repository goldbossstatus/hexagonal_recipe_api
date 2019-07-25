from api.api_users import UserAPI
from component_db.sqlite_storage import UserStorageSQLite

# connect UserStorageSQLite to user api

api = UserAPI(UserStorageSQLite(), 'key')

print(api.read('user_id', api_key='key'))


