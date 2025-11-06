import os
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

class Settings:
    
    dotenv_path = Path('/.env')
    load_dotenv(dotenv_path=dotenv_path)
    
    # Application
    APP_NAME: str = os.getenv("PROJECT_NAME", "None")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    HOST: str = os.getenv("API_HTTP_HOST", "0.0.0.0")
    PORT: int = int(os.getenv("API_HTTP_PORT", 8080))
    API_VERSION: str = os.getenv("API_VERSION", "/api/v1")
    
    # Concurrency
    MAX_WORKERS: int = int(os.getenv("MAX_WORKERS", 4))
    GRACEFUL_TIMEOUT: int = int(os.getenv("GRACEFUL_TIMEOUT", 4))
    TIMEOUT: int = os.getenv("WORKERS_TIMEOUT", 120)
    KEEPALIVE: int = os.getenv("WORKERS_KEEPALIVE", 5)
    MAX_REQUESTS: int = os.getenv("WORKERS_MAX_REQUESTS", 1000)
    REQUESTS_JITTER : int = os.getenv("WORKERS_REQUESTS_JITTER", 100)
    RELOAD: bool = DEBUG
    
    #Log
    ACCESSLOG: str = os.getenv("ACCESSLOG", "-")
    ERRORLOG = os.getenv("ERRORLOG", "-")
    LOGLEVEL = os.getenv("LOGLEVEL", "debug")
    
    #ML Model
    BalancingT1= os.getenv("Model_BalancingT1", "/app/model/t1_model.pkl")
    BalancingT2 = os.getenv("Model_BalancingT2", "/app/model/t2_model.pkl")
    BalancingT3 = os.getenv("Model_BalancingT3", "/app/model/t3_model.pkl")
    
settings = Settings()