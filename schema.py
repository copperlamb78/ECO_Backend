from pydantic import BaseModel
from typing import Optional, List

class PontoColetaCreat(BaseModel):
    nome: str
    endereco: str
    cidade: str
    estado: str
    latitude: float
    longitude: float
    telefone: Optional[str] = None
    horario: Optional[str] = None
    site: Optional[str] = None
    tipos_residuo: Optional[List[str]] = None

class PontoColetaResponse(BaseModel):
    id: int
    nome: str
    endereco: Optional[str]
    cidade: Optional[str]
    estado: Optional[str]
    telefone: Optional[str]
    horario: Optional[str]
    distancia_metros: Optional[float]