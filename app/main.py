from fastapi import FastAPI
from app.routes import destinations
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(destinations.router, prefix="/destinations", tags=["Destinations"])
