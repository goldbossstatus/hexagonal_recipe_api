from component_interface.persitent import IJwtStorage, IUserStorage
from api.api_models import User


class UserStorageSQLite(IUserStorage):
    # implement  sql lite storage for users

    def read(self, user_id: str):
        return User(user_password='hashed',
                    user_email='du@d.com')


class JwtStorageSQLite(IJwtStorage):
    # implement sqlite storage for  tokens
    pass

