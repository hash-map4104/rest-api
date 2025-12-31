from fastapi import FastAPI 
from .import models
from .database import engine
from .routers import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware



from alembic import command
from alembic.config import Config
import os

alembic_cfg = Config("alembic.ini")
command.upgrade(alembic_cfg, "head")



# ---------------------------------------------------------------
# Create tables if not already created
# This should only be used in development – in production we use Alembic migrations
# ---------------------------------------------------------------
# no need to use this if you are using alembic
# models.Base.metadata.create_all(bind=engine)
 
app = FastAPI()

# cors policy is set to allow people from google.com to talk to us
# * means every domain canuse this 
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)




#this will include our post.router 

