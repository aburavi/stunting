from pydantic import BaseModel
from typing import Optional

class Kategorikal(BaseModel):
    kategori_usia: Optional[str]
    kategori_pendidikan: Optional[str]
    kategori_pekerjaan: Optional[str]
    imt_prahamil: Optional[str]
    kek: Optional[str]
    kategori_kunjungan_anc: Optional[str]
    kategori_paritas: Optional[str]
    kategori_kenaikanbb: Optional[str]
    anemia: Optional[str]

class StuntingRisk(BaseModel):
    usia_ibu: Optional[int]
    lila: Optional[int]
    kategorikal: Optional[Kategorikal]
