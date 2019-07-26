import jwt

# models and serializers


class BaseModel:

    @classmethod
    def from_dict(cls, d):
        for field_name, field_type in cls.FIELD_TYPES.items():
            if d[field_name] is not None and not isinstance(d[field_name], field_type):
                raise TypeError(f'field: {field_name} have to be type: {cls.FIELD_TYPES[field_name]}')
        d = {k: d[k] for k in cls.FIELD_TYPES}
        return cls(**d)

    def to_dict(self):
        raise NotImplemented('to_dict method should be implemented')

    def __repr__(self):
        return f'{self.__class__.__name__}:{str(self.to_dict())}'


class JwtToken(BaseModel):
    FIELD_TYPES = {
        'user_id': str,
        'user_password': str,
        'expiration_ts': int
    }
    JWT_ALGO = 'HS256'

    def __init__(self,
                 user_id: str,
                 user_password: str,
                 expiration_ts: int = None,):

        self.user_id = user_id
        self.user_password = user_password
        self.expiration_ts = expiration_ts

    def to_dict(self):
        return {key: getattr(self, key) for key in self.FIELD_TYPES}

    @property
    def jwt(self):
        return jwt.encode(self.to_dict(), self.user_password, algorithm=self.JWT_ALGO).decode()

    def verify(self, jwt_st: str):
        if self.user_password:
            d = jwt.decode(jwt_st, self.user_password, algorithms=self.JWT_ALGO)
            if d and isinstance(d, dict) and 'user_password' in d:
                if d['user_password'] == self.user_password:
                    return True
            else:
                # return False
                raise ValueError('decode error')
        else:
            raise ValueError('no password in jwt token')
        return False


class Jwt(BaseModel):
    FIELD_TYPES = {
        'jwt': str,
        'user_id': str,
        'expiration_ts': int
    }
    jwt = None
    user_id = None
    expiration_ts = None

    def __init__(self,
                 jwt: str,
                 user_id: str,
                 expiration_ts: int = None,):

        self.jwt = jwt
        self.user_id = user_id
        self.expiration_ts = expiration_ts

    def to_dict(self):
        return {key: getattr(self, key) for key in self.FIELD_TYPES}


class User(BaseModel):
    FIELD_TYPES = {
        'user_id': str,
        'user_email': str,
        'first_name': str,
        'last_name': str,
        'user_password': str,

    }
    user_id = None
    user_email = None
    user_password = None
    first_name = None
    last_name = None

    def __init__(self,
                 user_id: str,
                 user_password: str,
                 user_email: str = None,
                 first_name: str = None,
                 last_name: str = None,):

        self.user_id = user_id
        self.user_email = user_email
        self.user_password = user_password
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {key: getattr(self, key) for key in self.FIELD_TYPES}


class Ingredient(BaseModel):
    pk_id = None
    name = None

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {'name': self.name}


class Tag(BaseModel):
    FIELD_TYPES = {
        'name': str,
    }
    pk_id = None
    name = None

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {key: getattr(self, key) for key in self.FIELD_TYPES}


class Recipe(BaseModel):
    FIELD_TYPES = {
        'recipe_id': str,
        'title': str,
        'time_minutes': str,
        'price': float,
        'tax': float,
        'ingredients': list,
        'tags': list
    }
    recipe_id = None
    title = None
    time_minutes = None
    price = None
    tax = None
    ingredients = None
    tags = None

    def __init__(self,
                 title: str,
                 time_minutes: int,
                 price: float,
                 tax: float,
                 ingredients: list,
                 tags: list,
                 ):
        self.title = title
        self.time_minutes = time_minutes
        self.price = price
        self.tax = tax
        self.tags = tags
        self.ingredients = ingredients

    def to_dict(self):
        d = {key: getattr(self, key) for key in self.FIELD_TYPES}
        d['ingredients'] = d['ingredients'].to_dict()
        d['tags'] = d['tags'].to_dict()

    @classmethod
    def from_dict(cls, d: dict):
        d['ingredients'] = [Ingredient.from_dict(item) for item in d['ingredients']]
        d['tags'] = [Tag.from_dict(item) for item in d['tags']]
        return cls(**d)
