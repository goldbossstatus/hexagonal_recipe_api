from api import api_models


class IAuthAPI:
    @staticmethod
    def authenticate(user_name: str, password: str) -> str:
        raise NotImplemented

    @staticmethod
    def revoke(user_name: str, password: str, jwt: str) -> bool:
        raise NotImplemented

    @staticmethod
    def is_expired(jwt: str) -> bool:
        raise NotImplemented

    @staticmethod
    def is_authenticated(jwt: str) -> bool:
        raise NotImplemented


class IUserAPI:

    def create(self, user: api_models.User, api_key: str = None):
        raise NotImplemented

    def read(self, user_id: str, api_key: str = None) -> api_models.User:
        raise NotImplemented

    def update(self, user_id: str, user: api_models.User, api_key: str = None):
        raise NotImplemented

    def delete(self, user_id: str, api_key: str = None):
        raise NotImplemented


class IUserReadApi:
    def read(self, user_id: str, api_key: str = None) -> api_models.User:
        raise NotImplemented


class IURecipeAPI:
    @staticmethod
    def create(user: api_models.Recipe, jwt: str = None):
        raise NotImplemented

    @staticmethod
    def read(recipe_id: str, jwt: str = None) -> api_models.Recipe:
        raise NotImplemented

    @staticmethod
    def update(recipe_id: str, recipe: api_models.Recipe, jwt: str = None):
        raise NotImplemented

    @staticmethod
    def delete(recipe_id: str, jwt: str = None) -> api_models.Recipe:
        raise NotImplemented
