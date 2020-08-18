### ITF SCRAPERS
Scraper to scrape tournament info from the ITF website.
#### Setting up chromedriver
- After cloning this repo
```
$ cd itf-scrapers
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export PATH:$PATH:/present/working/directory/of/this/repo
$ sudo apt-get install -f
```
#### About 
- This directory includes
    * Scraping scripts of
        1. ITF Tournaments - scrapeITF_Tourna.py
        2. FSC Tournaments - scrapeFSC.py
        3. Player Ranks - playerRankscraper.py

    * JSON files of 
        1. ITF Tournaments - itf_seniors.json
        2. FSC Tournaments - fsc.json
        3. Player Ranks - PlayerRanks.json

    * Psychopg File i.e. JSON to database scripts
        1. ITF Tournaments - ItfTournaToDb.py
        2. FSC Tournaments - fsctodb.py
        3. Player Ranks - PlayerRanktodb.py

- The scraping scripts scrape the respective events and make a repsective json file.
- The TODB files load the data from the json files to the respective tables in the database.
- To load the data change the file permission of load_real_data.sh  
    ```
    $chmod +x load_real_data.sh
    $./load_real_data.sh 
    ```
#### Setting up Cron Jobs
- Move all the cron_* files a directory below the itf-scrapers directory
