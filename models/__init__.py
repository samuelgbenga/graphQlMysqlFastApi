from . import user
from config import database

user.Base.metadata.create_all(bind=database.engine)