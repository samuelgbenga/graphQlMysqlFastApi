from fastapi import FastAPI
from graphql.schemas import graphql_app  # Import your custom GraphQL router


app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)