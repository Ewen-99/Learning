import psycopg2
from dotenv import load_dotenv
import os
import random

load_dotenv()
conn = psycopg2.connect(host='localhost', dbname='test', user='ewen', password=os.getenv("DB_PASSWORD"), port=5432)
cur = conn.cursor()


cur.execute("""
     CREATE TABLE IF NOT EXISTS new_car(
     car_uid UUID PRIMARY KEY,
     make VARCHAR(50) NOT NULL,
     price NUMERIC(19, 2) NOT NULL CHECK (price > 0)
     );
""")


makers = ['Mercury', 'Ford', 'Nissan', 'GMC', 'Land Rover']

for i in range(10):
    cur.execute("""
    INSERT INTO new_car (car_uid, make, price) VALUES (uuid_generate_v4(), %s, %s);    
""", (random.choices(makers)[0], random.randint(10**4, 10**6)))


sql_command = cur.mogrify("SELECT * FROM new_car LIMIT 5")
print(sql_command)

cur.execute("""
    SELECT * FROM new_car LIMIT 5;
""")

# print(cur.fetchone())
# print(cur.fetchall())

for row in cur.fetchall():
    print(row)
    print(type(row))    # tuple, starting from id/uid
    
conn.commit()

cur.close()
conn.close()
