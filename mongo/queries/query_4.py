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
pprint.pprint(list(listings.aggregate(pipeline)))

# Results:
# [{'_id': {'id': 38459934,
#           'name': 'Corporate Stays',
#           'url': 'https://www.airbnb.com/users/show/38459934'},
#   'listings': 169},
#  {'_id': {'id': 292507076,
#           'name': 'Luckey',
#           'url': 'https://www.airbnb.com/users/show/292507076'},
#   'listings': 77},
#  {'_id': {'id': 28047654,
#           'name': 'Yan',
#           'url': 'https://www.airbnb.com/users/show/28047654'},
#   'listings': 72},
#  {'_id': {'id': 72761895,
#           'name': 'Samuel',
#           'url': 'https://www.airbnb.com/users/show/72761895'},
#   'listings': 70},
#  {'_id': {'id': 304507661,
#           'name': 'Sonia',
#           'url': 'https://www.airbnb.com/users/show/304507661'},
#   'listings': 53},
#  {'_id': {'id': 111294431,
#           'name': 'Magdalina ( OLIT )',
#           'url': 'https://www.airbnb.com/users/show/111294431'},
#   'listings': 52},
#  {'_id': {'id': 487327,
#           'name': 'Louis',
#           'url': 'https://www.airbnb.com/users/show/487327'},
#   'listings': 51},
#  {'_id': {'id': 387422,
#           'name': 'Simplissimmo',
#           'url': 'https://www.airbnb.com/users/show/387422'},
#   'listings': 47},
#  {'_id': {'id': 73995257,
#           'name': 'Liv Mtl',
#           'url': 'https://www.airbnb.com/users/show/73995257'},
#   'listings': 47},
#  {'_id': {'id': 50780342,
#           'name': 'Emanuel',
#           'url': 'https://www.airbnb.com/users/show/50780342'},
#   'listings': 44}]