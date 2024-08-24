import strawberry
from fastapi import FastAPI, Depends, HTTPException
from strawberry.fastapi import GraphQLRouter
from schemas.index  import UserInput, User
from config.database import SessionLocal, get_db
from models.index import users



@strawberry.type
class Query:
    @strawberry.field
    def all_users(self, db = Depends(get_db)) :
        all_user = db.execute(users.select()).fetchall()

        result = []
        for user in all_user:
            user_dict = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                # Add other fields as necessary
            }
            result.append(user_dict)

        return result


@strawberry.type
class Mutation:
    @strawberry.mutation
    def register_user(self, user: UserInput, db = Depends(get_db)):
        # Check if the user already exists by email
        existing_user = db.execute(
            users.select().where(users.c.email == user.email)
        ).fetchone()

        if existing_user:
            # If user exists, raise an HTTPException
            raise HTTPException(status_code=400, detail="User already exists")

        db.execute(
            users.insert().values(
                name = user.name,
                email = user.email,
                password = user.password
            )
        )
        db.commit()
        return {"message": "User created successfully"}
    


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)