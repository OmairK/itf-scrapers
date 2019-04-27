#### Instructions 
- This directory includes
    * Scraping scripts of
        1. ITF Tournaments - scrapeITF_Tourna.py
        2. FSC Tournaments - scrape FSC.py
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
- Use the fsc virtual env
- To load the data change the file permission of load_real_data.sh  
    ```
    $chmod +x load_real_data.sh
    $./load_real_data.sh 
    ```
