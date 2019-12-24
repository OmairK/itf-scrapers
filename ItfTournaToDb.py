import psycopg2
import json


f = open("itf_seniors.json","r")
tournament_json = json.load(f)


months  = {'Jan': '01' ,'Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
def month_to_int(mon):
    for k in months:
        if k == mon:
            mon  = months[k]
            return mon


conn = psycopg2.connect(database="fsc_database", user="postgres",host='127.0.0.1', password="test123",port=5432)
cur = conn.cursor()
cur.execute('truncate table tournaments_tournamentitf')
conn.commit()


for lines in tournament_json:
    lst = [None]*9
    lst[0] = lines['Name']
    lst[1] = lines['Host nation:']
    a = lines['Date:']
    b=a.split(':')
    # print(a)
    # print(b)
    c=b[0].rstrip('\n')
    startDate,endDate = c.split("to")
    startDateDay,startDateMonth = startDate.split() ### different date formats for use in the flutter app
    endDateDay,endDateMonth,Year = endDate.split()
    STM = month_to_int('{}'.format(startDateMonth))
    ETM = month_to_int('{}'.format(endDateMonth))
    startDateInt = Year + STM + startDateDay
    endDateInt = Year + ETM + endDateDay
    
    print(startDateInt)
    # print(endDateInt)   
    lst[2] = startDateInt
    lst[3] = endDateInt
    lst[4] = lines['Category']
    lst[6] = lines['Venue:']
    lst[5] = lines['Surface:']
    lst[8] = lines['url']
    
    if "Website:" in lines:
        lst[7] = lines['Website:']
    

    cur.execute("INSERT INTO tournaments_tournamentitf(tournament_name,host_nation,grade,start_date,end_date,surface,venue,website,link) VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s)",(lst[0],lst[1],lst[4],lst[2],lst[3],lst[5],lst[6],lst[7],lst[8]))
    conn.commit()

cur.execute("SELECT * FROM tournaments_tournamentitf;")
cur.fetchone()
conn.commit()
cur.close()
conn.close()
print("ITF TOURNAMENTS TO DB: CODE 200")