### ITF SCRAPERS
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
<<<<<<< HEAD
        2. FSC Tournaments - scrapeFSC.py
=======
        2. FSC Tournaments - scrape FSC.py
>>>>>>> 8ed82e7d64cfdfaf8bbe86ef5a43c07363459403
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
<<<<<<< HEAD
=======
- Use the fsc virtual env
>>>>>>> 8ed82e7d64cfdfaf8bbe86ef5a43c07363459403
- To load the data change the file permission of load_real_data.sh  
    ```
    $chmod +x load_real_data.sh
    $./load_real_data.sh 
    ```
