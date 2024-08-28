from pydoc import resolve
import strawberry

from strawberry.fastapi import GraphQLRouter

from .schemas import User

from .resolver import QueryResolver, MutationResolver

from typing import List


@strawberry.type
class Query:
    users: List[User]|None = strawberry.field(resolver=QueryResolver.get_users)
    user: User|None = strawberry.field(resolver=QueryResolver.get_user)


@strawberry.type
class Mutation:
    add_user: User|None = strawberry.field(resolver=MutationResolver.add_user)
    edit_user: User|None = strawberry.field(resolver=MutationResolver.edit_user)
    delete_user: User| None = strawberry.field(resolver=MutationResolver.delete_user)


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

