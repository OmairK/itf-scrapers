import psycopg2
import json

conn = psycopg2.connect(database="fsc_database", user="postgres",host='127.0.0.1', password="test123",port=5432)
curr = conn.cursor()

playerR = open('fsc.json','r')
playerJs = json.load(playerR)

for lines in playerJs:
    a = lines['Event Name']
    b = lines['Under Group Name']
    c = lines['Venue Name']
    d = lines['Date']
    e = lines['Description']
    curr.execute("INSERT INTO tournaments_tournamentfsc(tournament_name,age_group,tournament_venue,date,tournament_description) VALUES (%s, %s,%s,%s, %s)",(a,b,c,d,e))
    conn.commit()

print('FSC TO DB : CODE 200')

curr.close()
conn.close()
