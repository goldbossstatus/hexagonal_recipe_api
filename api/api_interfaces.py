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
    def create(self, recipe: api_models.Recipe, jwt: str = None):
        raise NotImplemented

    def read(self, recipe_id: str, jwt: str = None) -> api_models.Recipe:
        raise NotImplemented

    def update(self, recipe_id: str, recipe: api_models.Recipe, jwt: str = None):
        raise NotImplemented

    def delete(self, recipe_id: str, jwt: str = None) -> api_models.Recipe:
        raise NotImplemented
