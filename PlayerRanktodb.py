import psycopg2
import json

conn = psycopg2.connect(database="fsc_database", user="postgres",host='127.0.0.1', password="test123",port=5432)
curr = conn.cursor()

curr.execute("Truncate table tournaments_playerrankingsms")
conn.commit()

playerR = open('PlayerRanks.json' , 'r')
playerJs = json.load(playerR)

for lines in playerJs:
    a = lines['Rank']
    b = lines['Player']
    c = lines['Movement']
    e = lines['DOB']
    f = lines['Events']
    g = lines['Points']
    h = lines['Age Group']
    d = lines['Type'] 
    curr.execute("INSERT INTO tournaments_playerrankingsms(name,rank,movement,dob,events,points,age_group,category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(b,a,c,e,f,g,h,d))
    conn.commit()

print('Player Rank To DB : CODE 200')

curr.close()
conn.close()
