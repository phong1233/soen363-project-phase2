# Find the the number of listings per room type

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]

pipeline = [
    { "$group": { "_id": "$room_type", "listings": { "$sum": 1 } }, },
    { "$sort": { "listings": 1 } }
]

import pprint
import datetime

a = datetime.datetime.now()
res = list(listings.aggregate(pipeline))
b = datetime.datetime.now()

c = b - a
pprint.pprint(res)
pprint.pprint(str(c.microseconds * 0.001) + ' ms')

# Results:
# [{'_id': 'Hotel room', 'listings': 146},
#  {'_id': 'Shared room', 'listings': 378},
#  {'_id': 'Private room', 'listings': 9757},
#  {'_id': 'Entire home/apt', 'listings': 21987}]
# '126.997 ms'