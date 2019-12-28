import time
import random
import requests
import os
import json
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)


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
        for age in range(35, 71, 5):
            randoms = random.randrange(51, 99)
            url = f"https://www.itftennis.com/Umbraco/Api/PlayerRankApi/GetPlayerRankings?circuitCode=VT&playerTypeCode=M&matchTypeCode=S&ageCategoryCode=V35&nationCode=IND%20%20%20%20%20&take={randoms}&skip=0"
            driver.get(url)
            xml_scraper(age, category, driver.page_source)


def xml_scraper(age, category, xml_txt):

    large_list = []
    xml_txt = BeautifulSoup(xml_txt, 'lxml')

    players = xml_txt.find_all('playerrankingapimodel')
    print(players)
    for player in players:
        loc_player = {'Rank': None, 'Player': None, 'Movement': None, 'Nation': 'IND',
                      'DOB': None, 'Events': None, 'Points': None, 'Age Group': age, 'Type': category}

        loc_player['Rank'] = player.find('rank').text
        loc_player['DOB'] = player.find('birthyear').text
        loc_player['Player'] = player.find('playerfamilyname').text
        loc_player['Movement'] = player.find('rankmovement').text
        loc_player['Events'] = player.find('tournamentsplayed').text
        loc_player['Points'] = player.find('points').text
        local_player_list.append(loc_player)
        print(json.dumps(local_player_list))
        


def driver_code():
    get_urls()
    
    with open('PlayerRanks.json','w') as file:
        file.write(json.dumps(local_player_list))



    

driver_code()
