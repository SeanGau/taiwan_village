SECRET_KEY = ''
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/village'
SQLALCHEMY_ENGINE_OPTIONS = {'encoding': 'utf-8', 'json_serializer': lambda obj: obj, 'echo': False}
SQLALCHEMY_TRACK_MODIFICATIONS = False
SESSION_PERMANENT = False