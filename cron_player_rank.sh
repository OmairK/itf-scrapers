#!/bin/bash
source ~/scrapervenv/bin/activate && export PATH=$PATH:/home/fsc/itf-scrapers
cd ~/itf-scrapers
chmod +x load_ranks.sh
./load_ranks.sh