# Find the host with the most amount of listings
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]

pipeline = [
  { "$group": { "_id": { "id": "$host_id", "name": "$host_name", "url": "$host_url" }, "listings": { "$sum": 1 }} },
  { "$sort": { "listings": -1 } },
  { "$limit": 10 }
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
# [{'_id': {'id': 38459934,
#           'name': 'Corporate Stays',
#           'url': 'https://www.airbnb.com/users/show/38459934'},
#   'listings': 200},
#  {'_id': {'id': 23693320,
#           'name': 'Reception From Lofts Vieux-Québec',
#           'url': 'https://www.airbnb.com/users/show/23693320'},
#   'listings': 78},
#  {'_id': {'id': 292507076,
#           'name': 'Luckey',
#           'url': 'https://www.airbnb.com/users/show/292507076'},
#   'listings': 77},
#  {'_id': {'id': 10202618,
#           'name': 'Simply Comfort',
#           'url': 'https://www.airbnb.com/users/show/10202618'},
#   'listings': 72},
#  {'_id': {'id': 28047654,
#           'name': 'Yan',
#           'url': 'https://www.airbnb.com/users/show/28047654'},
#   'listings': 72},
#  {'_id': {'id': 72761895,
#           'name': 'Samuel',
#           'url': 'https://www.airbnb.com/users/show/72761895'},
#   'listings': 70},
#  {'_id': {'id': 1919294,
#           'name': 'Toronto Suite Rentals',
#           'url': 'https://www.airbnb.com/users/show/1919294'},
#   'listings': 64},
#  {'_id': {'id': 34462857,
#           'name': 'Les Immeubles Charlevoix Courtier',
#           'url': 'https://www.airbnb.com/users/show/34462857'},
#   'listings': 63},
#  {'_id': {'id': 152088065,
#           'name': 'Gennadi',
#           'url': 'https://www.airbnb.com/users/show/152088065'},
#   'listings': 59},
#  {'_id': {'id': 785826,
#           'name': 'Arlene',
#           'url': 'https://www.airbnb.com/users/show/785826'},
#   'listings': 55}]
# '162.00300000000001 ms'