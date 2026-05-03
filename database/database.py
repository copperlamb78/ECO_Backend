from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from supabase import create_client
import os

load_dotenv()

URL_API = os.getenv("URL_API")
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_KEY = os.getenv("DATABASE_KEY")
supabase = create_client(URL_API, DATABASE_KEY)
