import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

GCP_MYSQL_HOSTNAME = os.getenv('GCP_MYSQL_USER')
GCP_MYSQL_USER = os.getenv('GCP_MYSQL_USER')
GCP_MYSQL_PASSWORD = os.getenv('GCP_MYSQL_USER')
GCP_MYSQL_DATABASE = os.getenv('GCP_MYSQL_USER')

connection_string = f'mysql'
engine = create_engine(connection_string)

##show databases
print(engine.table_names())