import strawberry
from strawberry.fastapi import GraphQLRouter
from config.database import get_db

class CustomGraphQLRouter(GraphQLRouter):
    def __init__(self, schema: strawberry.Schema, db):
        super().__init__(schema)
        self.db = db

    async def __call__(self, scope, receive, send):
        if scope['type'] == 'http':
            context = {'db': self.db}
            scope['context'] = context
        await super().__call__(scope, receive, send)
