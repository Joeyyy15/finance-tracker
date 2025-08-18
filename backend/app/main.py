from fastapi import FastAPI
from app.api.routes import router as api_router

from app.db.db_setup import Base, engine
from app.models import transaction

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Finance Tracker API is running!"}

#creates the database tables on startup
Base.metadata.create_all(bind = engine)