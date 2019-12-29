import time
import random
import requests
import os
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)


def get_urls():
    """
    Generate urls for scraping the xml data and passes the page source
    into xml_scraper
    """
    all_players = []
    categories = ['S', 'D']
    for category in categories:
        for age in range(35, 85, 5):
            randoms = random.randrange(70, 99)
            url = f"https://www.itftennis.com/Umbraco/Api/PlayerRankApi/GetPlayerRankings?circuitCode=VT&playerTypeCode=M&matchTypeCode=S&ageCategoryCode=V{age}&nationCode=IND%20%20%20%20%20&take={randoms}&skip=0"
            driver.get(url)
            all_players += xml_scraper(age, category, driver.page_source)
    return all_players


def xml_scraper(age, category, xml_txt):
    """
    Scrapes the details of each player from xml data and puts it in a list
    """
    players_w_same_category=[]
    xml_txt=BeautifulSoup(xml_txt, 'lxml')
    players=xml_txt.find_all('playerrankingapimodel')

    for player in players:
        loc_player={'Rank': None, 'Player': None, 'Movement': None, 'Nation': 'IND',
                      'DOB': None, 'Events': None, 'Points': None, 'Age Group': age, 'Type': category}

        loc_player['Rank'] = player.find('rank').text
        loc_player['DOB'] = player.find('birthyear').text
        loc_player['Player'] = player.find('playerfamilyname').text
        loc_player['Movement'] = player.find('rankmovement').text
        loc_player['Events'] = player.find('tournamentsplayed').text
        loc_player['Points'] = player.find('points').text

        players_w_same_category.append(loc_player)

    return players_w_same_category


def driver_code():
    """
    Main code block
    """
    player_dict = get_urls()

    with open('PlayerRanks.json', 'w') as file:
        file.write(json.dumps(player_dict))


if __name__ == '__main__':
    driver_code()
