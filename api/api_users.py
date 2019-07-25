from api import api_models
from api import api_interfaces
from component_interface import persitent
from component_db import sqlite_storage

class AuthenticationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.status = 403

# business logic for super admin
# accepts IStorage and api_key as input
# as functionality CRUD users


class UserAPI(api_interfaces.IUserAPI):

    def __init__(self, storage: persitent.IUserStorage, api_key: str):
        self._api_key = api_key
        self._storage = storage

    def _validate(self, api_key):
        if self._api_key != api_key:
            raise AuthenticationError('Authentication error')

    def create(self, user: api_models.User, api_key: str = None):
        self._validate(api_key)
        res = self._storage.create(user)
        return res

    def read(self, user_id: str, api_key: str = None) -> api_models.User:
        self._validate(api_key)
        res = self._storage.read(user_id)
        return res

    def update(self, user_id: str, user: api_models.User, api_key: str = None):
        self._validate(api_key)
        res = self._storage.read(user_id)
        return res

    def delete(self, user_id: str, api_key: str = None):
        self._validate(api_key)
        res = self._storage.delete(user_id)
        return res


class UserReadAPI(api_interfaces.IUserReadApi):
    def __init__(self, user_api: api_interfaces.IUserAPI, api_key: str = None):
        # mangled aka private
        self.__user_api = user_api
        self.__api_key = api_key

    def read(self, user_id: str, api_key: str = None) -> api_models.User:
        if not api_key:
            api_key = self.__api_key
        return self.__user_api.read(user_id, api_key=api_key)


class AuthAPI(api_interfaces.IAuthAPI):
    def __init__(self,
                 user_read: api_interfaces.IUserReadApi,
                 jwt_store: persitent.IJwtStorage):
        self.__user_read = user_read
        self.__jwt_store = jwt_store

    def authenticate(self, user_id: str, password: str) -> str:
        '''
        :param user_id:
        :param password:
        :return: jwt token
        '''

        user = self.__user_read.read(user_id)
        if not user:
            # todo raise user not found
            pass
        elif password != user.user_password:
            # todo raise auth err
            pass
        else:
            # todo JWT generator, expiration logic
            jwt = 'some.dummy.jwt'
            # todo transactional logic
            jwt_r = self.__jwt_store.create(jwt, user_id, expire_ts=0)
            return jwt_r

    # def revoke(self, user_name: str, password: str, jwt: str) -> bool:
    #     raise NotImplemented
    #
    # def is_expired(self, jwt: str) -> bool:
    #     raise NotImplemented
    #
    # def is_authenticated(self, jwt: str) -> bool:
    #     raise NotImplemented

