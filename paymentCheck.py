import psycopg2
from datetime import datetime as dt
from datetime import timedelta as td

conn = psycopg2.connect(database="fsc_database", user="postgres",
                        host='127.0.0.1', password="test123", port=5432)
cur = conn.cursor()
cur.execute("DELETE FROM payments_payment WHERE two_way_auth = 'O' AND date_time_of_payment+interval'600 seconds'< now();")
conn.commit()

cur.close()
conn.close()
