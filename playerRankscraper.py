from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import json


F = open("PlayerRanks.json" , "w")

options = Options()
options.add_argument("--headless")
options.add_argument("--no-proxy-server")
options.add_argument("--incognito")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")

driver = webdriver.Chrome(options = options)
driver.delete_all_cookies()
driver.implicitly_wait(10)
wait =WebDriverWait(driver,10)


keyP  = {1: 'Rank' ,2:'Player',3:'Movement',4:'Nation',5:'DOB',6:'Events',7:'Points',8:'AgeGroup'}
def keyint_to_Key(numb):
    for k in keyP:
        if k == numb:
            numb  = keyP[k]
            return numb

ageGroups = [35,40,45,50,55,60,65,70,75,80] ## Age Groups in Rankings
RankingType = ['S','D'] ##Singles or Doubles
AllPlayers = []

for types in RankingType:
  for ages in ageGroups:
    driver.quit()
    driver = webdriver.Chrome(options = options)

    url = 'https://www.itftennis.com/seniors/rankings/rankings-list/players.aspx?Gender=M&AgeGroup=V{}&Nation=IND&From=0&To=-1&Name=&Type={}'.format(ages,types) 
    def scrape(url):
      driver.get(url)
      html = driver.page_source
      driver.quit()
      soup = BeautifulSoup(html,"html.parser")
      counter = 0
      tr = soup.find_all('td')
      player = {}
      for data in tr:
        if data.text == '\n':
            if counter != 0:
              player.update({'Type' : '{}'.format(types)})
              player.update({'Age Group' : '{}'.format(ages)})
              AllPlayers.append(player.copy())
            counter = 0
        else:
          counter = counter + 1
          key = keyint_to_Key(counter)
          value = data.text.strip()
          player.update({'{}'.format(key) : '{}'.format(value)})

    scrape(url)
AllPlayers = json.dumps(AllPlayers)
F.write(AllPlayers)

