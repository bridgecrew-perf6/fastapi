from . import models
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .routers import post, user, auth, vote

from .config import settings


# tells sqlalchemy to run the create statement to generate all the tables when it firsts starts
# not needed if you use alembic, ok to leave it, but your first alembic migration (auto-generated) won't have anything since all
# the tables would already have been created
# note that sqlalchemy won't update an already existing table.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the battle star known as Galactica",
        "version": "0.0.2",
    }
