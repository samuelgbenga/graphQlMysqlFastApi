import strawberry
from schemas.index import UserInput, User
from models.index import users
from fastapi import HTTPException
from graphql.routes import CustomGraphQLRouter
from config.database import get_db

@strawberry.type
class Query:
    @strawberry.field
    def all_users(self, info) -> list[User]:
        db = info.context.get('db')
        if not db:
            raise HTTPException(status_code=500, detail="Database context is missing")

        all_users = db.execute(users.select()).fetchall()
        return [User(id=user.id, name=user.name, email=user.email) for user in all_users]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def register_user(self, user: UserInput, info) -> dict[str, str]:
        db = info.context.get('db')
        if not db:
            raise HTTPException(status_code=500, detail="Database context is missing")

        existing_user = db.execute(
            users.select().where(users.c.email == user.email)
        ).fetchone()

        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")

        db.execute(
            users.insert().values(
                name=user.name,
                email=user.email,
                password=user.password
            )
        )
        db.commit()
        return {"message": "User created successfully"}

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = CustomGraphQLRouter(schema=schema, db=next(get_db()))
