from sqlalchemy import Integer, String, Table, Column

#from config.database import meta

from config.database import Base

# users = Table(
#     'users', meta,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(50), nullable=False),
#     Column('email', String(100), nullable=False, unique=True),
#     Column('password', String(100), nullable=False)
# )

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)


    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, email={self.email})'