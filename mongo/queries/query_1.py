# Find the number of listings for each neighborhood
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]

pipeline = [
  { "$group": { "_id": "$neighbourhood_cleansed", "sum": { "$sum": 1 } }, },
  { "$sort": { "sum": -1 } },
  { "$limit": 5 }
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
# [{'_id': 'Ville-Marie', 'sum': 4069},
#  {'_id': 'Le Plateau-Mont-Royal', 'sum': 3603},
#  {'_id': 'Waterfront Communities-The Island', 'sum': 2776},
#  {'_id': 'Rosemont-La Petite-Patrie', 'sum': 1270},
#  {'_id': 'Côte-des-Neiges-Notre-Dame-de-Grâce', 'sum': 1041}]
# '116.99900000000001 ms'