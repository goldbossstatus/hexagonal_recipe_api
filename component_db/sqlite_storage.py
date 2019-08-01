from collections import defaultdict
from component_interface.persitent import IJwtStorage, IUserStorage
from api.api_models import User
from api.api_models import Jwt


class UserStorageSQLite(IUserStorage):
    # implement  sql lite storage for users

    def read(self, user_id: str):
        return User(user_password='hashed',
                    user_email='du@d.com')


class JwtStorageSQLite(IJwtStorage):
    # implement sqlite storage for  tokens
    pass


class UserStorageDict(IUserStorage):
    def __init__(self):
        self.__users = dict()

    @property
    def user_data(self):
        return {k: v for k, v in self.__users.items()}

    def create(self, user: User):
        if user.user_id not in self.__users:
            self.__users[user.user_id] = user.to_dict()

    def read_dict(self, user_id: str) -> dict:
        user_d = self.__users.get(user_id)
        return user_d

    def read(self, user_id) -> UserStorageSQLite:
        d = self.read_dict(user_id)
        if d:
            return User.from_dict(d)

    # def update(self, user_id, user: User):
    # #     raise NotImplemented
    # #
    # # def delete(self, user_id) -> User:
    # #     raise NotImplemented


class JwtStorageDict(IJwtStorage):
    def __init__(self):
        self.__data = dict()
        self.__users = dict()

    @property
    def users_data(self):
        return {k: v for k, v in self.__users.items()}

    @property
    def jwt_data(self):
        return {k: v for k, v in self.__data.items()}

    def create(self, jwt: Jwt):
        if jwt.jwt not in self.__data:
            self.__data[jwt.jwt] = jwt.to_dict()
            self.__users[jwt.user_id] = jwt.jwt

    def read_by_user(self, user_id) -> str:
        if user_id in self.__users:
            return self.__users[user_id]

    def read_by_jwt(self, jwt_st: str) -> Jwt:
        if jwt_st in self.__data:
            return Jwt.from_dict(self.__data[jwt_st])

    def delete(self, jwt_st: str) -> str:
        user_o = self.read_by_jwt(jwt_st=jwt_st)
        jwt_s = self.read_by_user(user_o.user_id)
        del self.__data[jwt_s]
        del self.__users[user_o.user_id]
        assert jwt_s == jwt_st
        return jwt_st
