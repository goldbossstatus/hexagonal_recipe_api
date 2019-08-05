from api import api_models
from api import api_interfaces
from component_interface import persitent
from component_db import sqlite_storage
import jwt

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
        # __mangled or private
        self.__user_api = user_api
        self.__api_key = api_key

    def read(self, user_id: str, api_key: str = None) -> api_models.User:
        if not api_key:
            api_key = self.__api_key
        return self.__user_api.read(user_id, api_key=api_key)


class AuthAPI(api_interfaces.IAuthAPI):
    def __init__(self,
                 user_store: persitent.ReadOnlyIUserStorage,
                 jwt_store: persitent.IJwtStorage):
        self.__user_store = user_store
        self.__jwt_store = jwt_store

    def authenticate(self, user_id: str, password: str) -> str:
        '''
        :param user_id:
        :param password:
        :return: jwt token string
        '''

        user = self.__user_store.read(user_id)
        if not user:
            # todo raise user not found
            pass
        elif password != user.user_password:
            # todo raise auth err
            pass
        else:
            # todo JWT generator, expiration logic
            jwt_token = api_models.JwtToken(
                user_id=user_id,
                user_password=password,
            )
            jwt_record = api_models.Jwt(
                jwt=jwt_token.jwt,
                user_id=user_id,
            )
            # todo transactional logic
            r = self.__jwt_store.create(jwt_record)
            return jwt_token.jwt

    def revoke(self, user_id: str, password: str, jwt_st: str) -> bool:
        jwt_o = self.__jwt_store.read_by_jwt(jwt_st)
        if jwt_o:
            user_o = self.__user_store.read(jwt_o.user_id)

            if jwt_o.user_id != user_id or user_o.user_password != password:
                return False

            jwt_s = self.__jwt_store.delete(jwt_st)
            assert jwt_s == jwt_st
            return True
        else:
            return False

    def is_authenticated(self, jwt_st: str) -> bool:
        jwt_record = self.__jwt_store.read_by_jwt(jwt_st)
        if jwt_record:
            user_record = self.__user_store.read(jwt_record.user_id)
            jwt_token = api_models.JwtToken(
                user_id=user_record.user_id,
                user_password=user_record.user_password,
            )
            return jwt_token.verify(jwt_st)

        return False

    def get_owner(self, jwt_st: str) -> api_models.User:
        jwt_record = self.__jwt_store.read_by_jwt(jwt_st)
        if jwt_record:
            user_record = self.__user_store.read(jwt_record.user_id)
            jwt_token = api_models.JwtToken(
                user_id=user_record.user_id,
                user_password=user_record.user_password,
            )
            verified = jwt_token.verify(jwt_st)
            if verified:
                user = api_models.User(user_id=user_record.user_id, user_password='')
                return user

    #
    # def is_expired(self, jwt: str) -> bool:
    #     raise NotImplemented
    #


class RecipeAPI(api_interfaces.IURecipeAPI):
    def __init__(self,
                 recipe_storage: persitent.IRecipeStorage,
                 auth: api_interfaces.IAuthAPI):
        self.__recipe_storage = recipe_storage
        self.__auth = auth

    def read(self, recipe_id: str, jwt_st: str = None) -> api_models.Recipe:
        model: api_models.Recipe
        owner: api_models.
        authenticated = self.__auth.is_authenticated(jwt_st=jwt_st)
        owner : api_models
        if not authenticated:
            raise ValueError('Not authenticated!')
        recipe_o = self.__recipe_storage.read(recipe_id)
        return recipe_o

    def