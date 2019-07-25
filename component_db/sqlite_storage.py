from component_interface.persitent import IJwtStorage, IUserStorage


class UserStorageSQLite(IUserStorage):
    # implement  sql lite storage for users
    pass


class JwtStorageSQLite(IJwtStorage):
    # implement sqlite storage for  tokens
    pass

