from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import xmltodict
import pprint
import xml.etree.ElementTree as ET
from math import ceil
from xmljson import badgerfish as bf
import requests
import random
import time


"""
options = Options()
options.add_argument("--headless")
options.add_argument("--no-proxy-server")
options.add_argument("--incognito")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options = options
driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()
driver.implicitly_wait(5)

chromedriver = "/home/omair/Downloads"
os.environ["webdriver.chrome.driver"] = chromedriver



Procedure:
    1) Input India in the Nation
    2) Iterate over the ageGroups 
"""




"""
Procedure
    1) Generate URls for all age groups
"""

itf_to_local_dict = {'rank': 'Rank', 'playerfamilyname': 'Player', 'rankmovement': 'Movement',
                     'birthYear': 'DOB', 'tournamentsplayed': 'Events', 'points': 'Points', 'Age Group': 'Age Group',
                     'Type': 'Type'}

local_player_list = []


def get_urls():
    """
    Generate urls for the url list
    """

    categories = ['S', 'D']
    for category in categories:
        for age in range(35,36 , 5):
            randoms = random.randrange(51,99)
            url = f"https://www.itftennis.com/Umbraco/Api/PlayerRankApi/GetPlayerRankings?circuitCode=VT&playerTypeCode=M&matchTypeCode=S&ageCategoryCode=V35&nationCode=IND%20%20%20%20%20&take={randoms}&skip=0"#&nationCode=IND
            # url = url.encode('utf-8')
            # print(url.decode('utf-8'))
            UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
                   "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
                   "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
                   )
            ua = UAS[random.randrange(len(UAS))]
            headers = {'user-agent': ua}
            response = requests.get(url=url, headers=headers)
            time.sleep(9)
            

            xml_scraper(age, category, response)
            time.sleep(9)


def xml_scraper(age, category, xml_txt):
    
    xml_txt = BeautifulSoup(xml_txt.text, 'lxml')

    print(xml_txt)
    players = xml_txt.find_all('playerrankingapimodel')
    print(players)
    for player in players:
        loc_player={'Rank':None,'Player':None,'Movement':None,'Nation':'IND','DOB':None,'Events':None, 'Points':None, 'AgeGroup':age,'Type':category}
        for attrib in player:
            tag = attrib.tag
            print(tag)
            loc_dict_key = itf_to_local_dict['%s' %(tag)]
            loc_player['%s' %(loc_dict_key)] = attrib.tag
            print(loc_player)
        local_player_list.append(loc_player)
            
    # print(a)
    #try:
    #root = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/div[1]/span[2]/text()[1]")
    #except Exception as e:
    #print(e)
    #print(root)
    #for neighbours in root.iter('Items'):
    #    print(neighbours.text)


def driver_code():
    get_urls()
    local_player_list = json.dumps(local_player_list)
    with open('PlayerRanks.json','w') as file:
        file.write(local_player_list)


if __name__ == '__main__':
    driver_code()
