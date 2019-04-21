
from bs4 import BeautifulSoup
import time
import requests
import re
import json

import psycopg2

conn = psycopg2.connect(database="mydatabase_phase1", user="postgres",host='127.0.0.1', password="test123",port=5432)
curr = conn.cursor()

for i in range (75,90):
    url="http://www.fansportsclub.com/Details.aspx?Eid=%d"%(i)
    res2 = requests.get(url)

    if(res2.status_code==200):
        
    
        soup = BeautifulSoup(res2.text,"html.parser")
        
        dl = soup.find('dl').find("table")
        #print(dl)
        tourn = []
        if dl is not None:
          
        
            table=soup.find_all('table')
            tr=table[4].find_all('tr')

            z = 0
            l = {}
            for x in tr:
                json_data = json.dumps({})
                if(z%2==0):
                    a = (x.text.strip())
                    b=a.split(' :- ')
                    
                    if(z!=8 and z!=6):
                        # json_data['das']='dasdas'
                        # json_data["{}".format(b[0])]="{}".format(b[1])
                        l['{}'.format(b[0])]=b[1]
                        print(b[0]+b[1])
                    elif(z==6):
                        d = b[1].split('/')
                        c = d[2]+d[1]+d[0].strip()
                        l['{}'.format(b[0])] = c



                    else:
                        #json_data["Description"]=b[0]
                        l['Description']=b[0]
                        # print(b[0])
                z=z+1

            # print(l['Description'])



            json_data = json.dumps(l)
            # print(json_data)
            json_load = json.loads(json_data)
            print(json_load['Date'])


        # z=0 => Event Name
        # z=2 => Venue Name
        # z=4 => Age Group
        # z=6 => Date
        # z=8 => Description
        # Apply Switch-Case inside if and make DB BBZ
            a = json_load['Event Name']
            b = json_load['Under Group Name']
            c = json_load['Venue Name']
            d = json_load['Date']
            e = json_load['Description']
            curr.execute("INSERT INTO tournaments_tournamentfsc(name,age_group,venue,date,description) VALUES (%s, %s,%s,%s, %s)",(a,b,c,d,e))
            conn.commit()

# f = open("FSC.json","w")
# f.write("{}".format(l))
curr.close()
conn.close()
