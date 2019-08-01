from api import api_models


class IAuthAPI:
    def authenticate(self, user_id: str, password: str) -> str:
        raise NotImplemented

    def revoke(self, user_id: str, password: str, jwt_st: str) -> bool:
        raise NotImplemented

    def is_expired(self, jwt_st: str) -> bool:
        raise NotImplemented

    def is_authenticated(self, jwt_st: str) -> bool:
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
