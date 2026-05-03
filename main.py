from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
import os
from dotenv import load_dotenv
import re
from math import radians, cos, sin, asin, sqrt
load_dotenv()

app = FastAPI()
router = APIRouter()
localhost1=os.getenv("localhost1")
localhost2=os.getenv("localhost2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, substitua "*" pelo domínio do seu frontend
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

URL_API = os.getenv("URL_API")
NEXT_PUBLIC_SUPABASE_URL = os.getenv("DATABASE_URL")
DATABASE_KEY = os.getenv("DATABASE_KEY")



supabase = create_client(URL_API, DATABASE_KEY )


@router.get("/")
def homepage():
    return {"mensagem": "ECO"}

@router.get("/addres")
def addres():
    return {"message": "página de localização"}

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000 # Raio da Terra em metros
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    a = sin(dLat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    return R * c

@router.get("/pontos")
def pontos(latitude: float = None, longitude: float = None, distancia_metros: float = 5000):
    response = supabase.table('pontos_de_coleta').select("*").execute()
    pontos_db = response.data
    
    if latitude is not None and longitude is not None:
        pontos_filtrados = []
        for p in pontos_db:
            loc = p.get("localizacao", "")
            p_lat, p_lon = None, None
            
            # Extrai a longitude e latitude do formato WKT: POINT(lon lat)
            if isinstance(loc, str):
                match = re.search(r"POINT\(([-\d\.]+)\s+([-\d\.]+)\)", loc)
                if match:
                    p_lon = float(match.group(1))
                    p_lat = float(match.group(2))
            
            if p_lat is not None and p_lon is not None:
                p["latitude"] = p_lat
                p["longitude"] = p_lon
                dist = haversine(latitude, longitude, p_lat, p_lon)
                p["distancia_metros"] = dist
                
                # Retorna apenas se estiver dentro do raio escolhido (5km)
                if dist <= distancia_metros:
                    pontos_filtrados.append(p)
        
        # Ordena dos mais próximos para os mais distantes
        pontos_filtrados.sort(key=lambda x: x["distancia_metros"])
        return {"pontos": pontos_filtrados}

    return {"pontos": pontos_db}

app.include_router(router)