from api.api_models import User


class IUserStorage:

    def create(self, user: User):
        raise NotImplemented

    def read(self, user_id: str):
        raise NotImplemented

    def update(self, user_id, user: User):
        raise NotImplemented

    def delete(self, user_id) -> User:
        raise NotImplemented


class IJwtStorage:

    def create(self, jwt: str, user_id: str, expire_ts: int):
        raise NotImplemented

    def delete(self, jwt: str) -> str:
        raise NotImplemented

