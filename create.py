#!/usr/local/bin/python3

import json
from datetime import datetime, date, time

my_feed = dict()

my_feed['providerName'] = "Galaxy3.net"
my_feed['language'] = "en-US"
my_feed['lastUpdated'] = datetime.now().astimezone().replace(microsecond=0).isoformat()
# https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python

my_feed['categories'] = [ {
    "name": "Cooking Shows",
    "query": "cooking AND reality shows",
    "order": "most_popular"
} ]

json_obj = json.dumps(my_feed, indent=4)

fh = open("feed.json", "w")

fh.write(json_obj)

fh.close()
