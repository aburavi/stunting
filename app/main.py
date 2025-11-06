from fastapi import FastAPI
from typing import Dict, List
from config import settings
from api.v1.endpoints import router as v1_router


app = FastAPI(
    title=settings.APP_NAME,
    description="This is a Stunting API for demonstrating FastAPI and OpenAPI.",
    version="1.0.0",
    openapi_url="/openapi/stunting-openapi.json", # Optional: customize the OpenAPI JSON endpoint
    docs_url="/openapi/docs",
    debug=settings.DEBUG
)

# Include routers
app.include_router(v1_router)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        workers=1 if settings.RELOAD else settings.MAX_WORKERS,
    )
    