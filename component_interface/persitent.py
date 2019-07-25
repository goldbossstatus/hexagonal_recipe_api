from api.api_models import User


class IUserStorage:

    @staticmethod
    def create(user: User):
        raise NotImplemented

    @staticmethod
    def read(user_id: str):
        raise  NotImplemented

    @staticmethod
    def update(user_id, user: User):
        raise NotImplemented

    @staticmethod
    def read(self, user_id):
        raise NotImplemented

    @staticmethod
    def delete(self, user_id) -> User:
        raise NotImplemented


class IJwtStorage:

    @staticmethod
    def create(jwt: str, user_id: str, expire_ts: int):
        raise NotImplemented

    @staticmethod
    def delete(jwt: str) -> str:
        raise NotImplemented

