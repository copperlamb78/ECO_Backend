from sqlalchemy import Table, Column, Integer, String, Boolean, ARRAY, MetaData
from geoalchemy2 import Geometry

metadata = MetaData ()

pontos_de_coleta = Table(
    "pontos_de_coleta",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nome", String(200), nullable=False),
    Column("endereco", String(400)),
    Column("cidade", String(100)),
    Column("estado", String(2)),
    Column("telefone", String(20)),
    Column("horario", String(200)),
    Column("site", String(300)),
    Column("tipos_residuo", ARRAY(String)),
    Column("localizacao", Geometry("POINT", srid=4326)),
    Column("ativo", Boolean, default=True),
)