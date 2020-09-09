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

my_feed['movies'] = [
{  
   "id":"1509428502952",
   "title":"Sample Movie",
   "content":{  
  	"dateAdded":  datetime.now().astimezone().replace(microsecond=0).isoformat(),
  	"videos": [
   	 {
       		"url": "https://mnmedias.api.telequebec.tv/m3u8/29880.m3u8",
       	  	"quality": "HD",
       	 	"videoType": "MP4"
     	 }
	]
   },
   "genres":[  
      "drama",
      "comedy",
      "horror"
   ],
   "thumbnail":"https://example.org/cdn/thumbnails/1509428502952/1",
   "releaseDate":"2016-01-01",
   "shortDescription":"Incredible movie description",
   "longDescription":"Even more incredible and longer movie description",
   "tags":[  
      "amazing",
      "drama",
      "comedy",
      "horror"
   ]
}]

json_obj = json.dumps(my_feed, indent=4)

fh = open("feed.json", "w")

fh.write(json_obj)

fh.close()
