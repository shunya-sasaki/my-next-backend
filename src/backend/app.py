from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager
from backend.routers.config import router as config_router
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(config_router)
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


def run():
    uvicorn.run(app, host="http://localhost", port=8000)
