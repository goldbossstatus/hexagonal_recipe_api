from api import api_models
from api import api_interfaces
from component_interface import persitent


class AuthenticationError(Exception):
    def __init__(self, message):
        super(self).__init__(message)
        self.status = 403

# business logic for super admin
# accepts IStorage and api_key as input
# as functionality CRUD users


class UserAPI(api_interfaces.IUserAPI):

    def __init__(self, storage: persitent.IUserStorage, api_key: str):
        self._api_key = api_key
        self._storage = storage

    def _validate(self, api_key):
        if self._api_key == api_key:
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