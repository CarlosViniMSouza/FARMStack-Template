from motor.motor_asyncio import AsyncIOMotorCursor as AsyncIO
from fastapi import FastAPI
from config import settings
import uvicorn

from apps.routers import router as todoRouter

app = FastAPI()
app.include_router(todoRouter, tags=["taks"], prefix="/task")


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI"}


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIO(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
