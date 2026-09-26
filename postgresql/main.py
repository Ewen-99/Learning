import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(host='localhost', dbname='test', user='ewen', password='ss', post=5432)