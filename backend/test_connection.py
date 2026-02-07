from sqlmodel import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.all())
