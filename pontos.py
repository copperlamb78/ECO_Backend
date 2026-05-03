import os
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

URL_API = os.getenv("URL_API")
DATABASE_KEY = os.getenv("DATABASE_KEY")

supabase = create_client(URL_API, DATABASE_KEY)

lista_de_pontos = [
    {
        "id":"1",
        "nome": "Vida Logística Reversa",
        "endereco": "Av. João Durval Carneiro, 2244 - Ponto Central, Feira de Santana - BA, 44075-196",
        "cidade": "Feira de Santana",
        "estado": "BA",
        "localizacao": "POINT(-38.949724171164824 -12.25291794458026)" # Formato WKT: POINT(longitude latitude)
    },
    {
        "id":"2",
        "nome": "NOGUEIRA RECICLAGEM",
        "endereco": "Rua Secundária, 45",
        "cidade": "Feira de Santana",
        "estado": "BA",
        "localizacao": "POINT(-38.91424055767034 -12.22768971947288)"
    },
    {
        "id":"3",
        "nome": "Eletrônica HCRecycling",
        "endereco": "Próximo a praça morena bela na rua do CMI - Tv. Abdon Costa - Ginásio, Serrinha - BA, 48700-000",
        "cidade": "Serrinha",
        "estado": "BA",
        "localizacao": "POINT(-39.00336007116483 -11.661128698497855)"  
    }
]

resposta = supabase.table("pontos_de_coleta").insert(lista_de_pontos).execute()

print(f"{len(resposta.data)} pontos foram incluídos com sucesso no banco de dados!")
