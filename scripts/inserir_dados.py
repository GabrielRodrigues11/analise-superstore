from dotenv import load_dotenv
import pandas as pd
import os
from sqlalchemy import create_engine


# Carregar senha do .env
load_dotenv("my.env")
senha = os.getenv("MYSQL_PASSWORD")

# Criar conexão com MySQL
engine = create_engine(f"mysql+pymysql://root:{senha}@localhost/superstore_db")

# Ler CSV
superstore_df = pd.read_csv("dados/brutos/superstore.csv", encoding="latin1")

# Inserir na tabela já criada no MySQL
superstore_df.to_sql("superstore_raw", engine, if_exists="append", index=False)
