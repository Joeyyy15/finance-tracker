from fastapi import FastAPI

# imports the router that holds all the endpoints
from app.api.routes import router as api_router

# imports SQLAlchemy Base and engine so we can create tables on startup
from app.db.db_setup import Base, engine

async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Finance Tracker API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Fiannce Tracker API is running."}

# mount all routes under /api
app.include_router(api_router, prefix="/api")
