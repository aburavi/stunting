from fastapi import APIRouter
from repository import StuntingRisk
import numpy as np
import pickle
from config import settings

# Load the trained model trimester-1
with open(settings.BalancingT1, "rb") as filet1:
    modelt1 = pickle.load(filet1)
# Load the trained model trimester-1
with open(settings.BalancingT2, "rb") as filet2:
    modelt2 = pickle.load(filet2)
# Load the trained model trimester-1
with open(settings.BalancingT3, "rb") as filet3:
    modelt3 = pickle.load(filet3)
    
router = APIRouter(prefix="/v1", tags=["v1"])

@router.get("/")
async def read_root():
    return {"status": "OK", "message": "Stunting Analyzer API!"}

@router.get("/health")
async def health_check():
    return {"status": "OK", "message": "Service is healthy"}

@router.get("/hello")
async def hello(name: str = "World"):
    return {"status": "OK", "message": f"Welcome to Stunting Analyzer!, Hello: {name}"}

@router.post("/predict")
async def predict(data: StuntingRisk):
    numerikal = np.array([[data.usia_ibu, data.lila,
                            data.kategorikal.kategori_usia,
                            data.kategorikal.kategori_pendidikan,
                            data.kategorikal.kategori_pekerjaan,
                            data.kategorikal.imt_prahamil,
                            data.kategorikal.kek,
                            data.kategorikal.kategori_kunjungan_anc,
                            data.kategorikal.kategori_paritas,
                            data.kategorikal.kategori_kenaikanbb,
                            data.kategorikal.anemia]])
    predictiont1 = modelt1.predict(numerikal)
    predictiont2 = modelt2.predict(numerikal)
    predictiont3 = modelt3.predict(numerikal)
    return {"status": "OK", "message": {
            "Predicted Stunting T1": predictiont1[0],
            "Predicted Stunting T2": predictiont2[0],
            "Predicted Stunting T3": predictiont3[0]}}