from os import name
from strawberry import ID
from . import schemas
from models import user
from typing import List
from config.database import SessionLocal

class QueryResolver:
    @staticmethod
    def get_users() -> List[schemas.User]:
        db = SessionLocal()
        try:
            query= db.query(user.User)
            users = query.all()
        finally:
            db.close()
       
        return users # type: ignore

    @staticmethod
    def get_user(user_id: ID) -> (schemas.User | None):
        db = SessionLocal()
        try:
            singleUser=db.query(user.User).filter(user.User.id==user_id).first()
        finally:
            db.close()
        
        return singleUser


class MutationResolver:
    @staticmethod
    def add_user(new_user: schemas.NewUser)-> schemas.User:
        db = SessionLocal()
        try:
            new = user.User(name=new_user.name, email=new_user.email, password=new_user.password)
            db.add(new)
            db.commit()
            db.refresh(new)
        finally:
            db.close()

        return new

    @staticmethod
    def edit_user(user_id: ID, e_user: schemas.UpdateUserInfo) -> schemas.User|None:
        db = SessionLocal()

        try:
            edit_user = db.query(user.User).filter(user.User.id==user_id).first()

            edit_user.name = e_user.name if e_user.name is None else edit_user.name # type: ignore

            edit_user.email = e_user.email if e_user.email is None else edit_user.email # type: ignore

            edit_user.password = e_user.password if e_user.password is None else edit_user.password # type: ignore
        
            db.commit()
            db.refresh(edit_user)

        finally:
            db.close

        #return "user edited"

    @staticmethod
    def delete_user(user_id: ID):

        db=SessionLocal()

        try:
            delete_user= db.query(user.User).filter(user.User.id == user_id).first()
            db.delete(delete_user)
            db.commit()
        finally:
            db.close()
        
        #return "user deleted"