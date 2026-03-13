from database import DATABASE_URL, engine #diz que tem erro, mas roda normal a API
from fastapi import APIRouter
from sqlalchemy import create_engine, text

router = APIRouter()

@router.get("/pontos")
def pontos_de_coleta(latitude: float ,longitude: float, distancia_metros: int = 5000):
    query = text("""
        SELECT id, 
        nome, 
        endereco, 
        cidade, 
        estado, 
        telefone, 
        horario, 
        site, 
        tipos_residuo, 
        localizacao, 
        ST_Distance(
            localizacao::geography,
            ST_SetSRID(ST_MakePoint(:lng, :lat), 4326)::geography
        ) AS distancia_metros
        FROM pontos_de_coleta 
        WHERE ativo = true 
        AND ST_DWithin(
            localizacao::geography,
            ST_SetSRID(ST_MakePoint(:lng, :lat), 4326)::geography,
            :distancia_metros
        )
        ORDER BY distancia_metros
    """)
    with engine.connect() as conn:
        resultado = conn.execute(query, {"lat": latitude, "lng": longitude, "distancia_metros": distancia_metros})
        pontos = [dict(row._mapping) for row in resultado]
    return {"total": len(pontos), "pontos": pontos}
