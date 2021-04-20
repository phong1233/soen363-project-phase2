# Find the average listing price per neighbourhood
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]

pipeline = [
  { "$group": { "_id": "$neighbourhood_cleansed", "avg_price": { "$avg": "$price" } }, },
  { "$sort": { "avg_price": -1 } },
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
# [{'_id': 'Kingsway South', 'avg_price': 194.4},
#  {'_id': "L'Île-Bizard-Sainte-Geneviève", 'avg_price': 192.73684210526315},
#  {'_id': 'Leaside-Bennington', 'avg_price': 175.30612244897958},
#  {'_id': 'Markland Wood', 'avg_price': 165.5},
#  {'_id': 'Lawrence Park South', 'avg_price': 165.14285714285714}]
# '135.621 ms'