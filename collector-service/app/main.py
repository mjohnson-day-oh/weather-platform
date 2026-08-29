from fastapi import FastAPI, status
from services import weatherCollector

base = FastAPI()

@base.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {
        "status": "healthy"
    }

@base.get("/collect")
async def get_obs():
    weatherCollector.get_all_observations()