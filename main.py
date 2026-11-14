from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager

from api import router as api_router
from core.config import settings

from core.models import db_helper

@asynccontextmanager
async def lifespan(_: FastAPI):

    yield

    await db_helper.dispose()

app = FastAPI(
    lifespan=lifespan
)
app.include_router(
    api_router,
    prefix=settings.api.prefix
)

if __name__ == '__main__':
    uvicorn.run(
        'main:app', 
        reload=True, 
        port=settings.run.port, 
        host=settings.run.host
)
