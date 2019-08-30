#!/bin/bash
source ~/scrapervenv/bin/activate && export PATH=$PATH:/home/fsc/itf-scrapers
cd ~/itf-scrapers
python3 paymentCheck.py 
