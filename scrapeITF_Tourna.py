import time
import os
import json
import requests
import re
import datetime
import pprint


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

dir = os.getcwd()

options = Options()
options.add_argument("--headless")
options.add_argument("--no-proxy-server")
options.add_argument("--incognito")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")


chromedriver = "/home/omair/Downloads"
os.environ["webdriver.chrome.driver"] = chromedriver


driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()

driver = webdriver.Chrome(options=options)


"""
Proceure:
    1) Generate urls for 12 coming months
    2) Scrape the data from each urls
    3) Maintain a pandas dataframe of all tournaments
    4) Convert it into a json format
"""


url_list = []


def generate_urls():
    """
    Appends genrated urls to the urls list
    """
    start_date = datetime.datetime.today()
    for i in range(12):
        start_date += datetime.timedelta(days=31)
        url = f"https://www.itftennis.com/en/tournament-calendar/seniors-tennis-tour-calendar/?startdate={start_date.year}-{start_date.month}"
        url_list.append(url)


tournaments_list = []


def text_scraper(page_html, url):
    """
    Scrapes the html from the page returned by the driver
    """

    tr = page_html.find_all('tr', class_="whatson-table__tournament")
    for i in range(len(tr)):
        tournament = {'Name': None, 'Host nation:': None, 'Date:': None, 'Surface': None,
                      'Venue': None, 'Category': None, 'Website:': None, 'url': None}
        tournament['Name'] = tr[i].find('td', class_='name').get_text('div')
        tournament['Date:'] = tr[i].find('td', class_='date').find(
            'span', class_='date').get_text()
        tournament['Host nation:'] = tr[i].find('td', class_='hostname').find(
            'span', class_='hostname').get_text()
        tournament['Venue'] = tr[i].find('td', class_='location').find(
            'span', class_='location').get_text()
        tournament['Category'] = tr[i].find('td', class_='category').find(
            'span', class_='category').get_text()
        tournament['Surface'] = tr[i].find('td', class_='surface').find(
            'span', class_='surface').get_text()
        if tr[i].find('td', class_='name').find('a').has_attr('href'):
            tournament['url'] = "https://www.itftennis.com" + tr[i].find(
                'td', class_='name').find('a').attrs['href']
        tournament['Website:'] = url
        tournaments_list.append(tournament.copy())


def show_more():
    """
    Clicks on the show more button to display all the 
    """
    delay = 4
    elements_left = True
    while(elements_left):
        try:
            driver.find_element_by_xpath(
                '/html/body/main/div[2]/div[2]/section/div/div/button').click()
        except NoSuchElementException as e:
            elements_left = False
            # print("All the tournaments are visible now")


def json_writer():
    """
    Writes the json of all tournaments to a file
    """
    global tournaments_list
    if(len(tournaments_list) != 0):
        tournaments_list = json.dumps(tournaments_list)
        with open('itf_seniors.json', 'w') as file:
            file.write(tournaments_list)
            print('File written')


def driver_code():
    """
    Executes the procedure 
    """
    generate_urls()
    for url in url_list:
        driver.get(url)
        show_more()
        html = BeautifulSoup(driver.page_source, 'html.parser')
        text_scraper(html, url)
    json_writer()


if __name__ == '__main__':
    driver_code()
