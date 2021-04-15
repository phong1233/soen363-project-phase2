# Find the host with the worst reviews
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]

pipeline = [
  { "$group": { "_id": { "id": "$host_id", "name": "$host_name", "url": "$host_url" }, "review_scores_rating": { "$avg": "$review_scores_rating"}, "reviews_per_month": { "$avg": "$reviews_per_month"} } },
  { "$unwind": "$review_scores_rating" },
  { "$sort": { "review_scores_rating": 1, "reviews_per_month": -1 } },
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
# [{'_id': {'id': 365201168,
#           'name': 'Amine',
#           'url': 'https://www.airbnb.com/users/show/365201168'},
#   'review_scores_rating': 20.0,
#   'reviews_per_month': 1.0},
#  {'_id': {'id': 264962284,
#           'name': 'Haimonti',
#           'url': 'https://www.airbnb.com/users/show/264962284'},
#   'review_scores_rating': 20.0,
#   'reviews_per_month': 1.0},
#  {'_id': {'id': 245910022,
#           'name': 'Daksh',
#           'url': 'https://www.airbnb.com/users/show/245910022'},
#   'review_scores_rating': 20.0,
#   'reviews_per_month': 0.94},
#  {'_id': {'id': 369329216,
#           'name': 'Lina',
#           'url': 'https://www.airbnb.com/users/show/369329216'},
#   'review_scores_rating': 20.0,
#   'reviews_per_month': 0.79},
#  {'_id': {'id': 259305857,
#           'name': 'Ozkr',
#           'url': 'https://www.airbnb.com/users/show/259305857'},
#   'review_scores_rating': 20.0,
#   'reviews_per_month': 0.76},
#  {'_id': {'id': 113245287,
#           'name': 'Aline',
#           'url': 'https://www.airbnb.com/users/show/113245287'},
#   'review_scores_rating': 20.0,
#   'reviews_per_month': 0.55},
#  {'_id': {'id': 341982673,
#           'name': 'Olivier',
#           'url': 'https://www.airbnb.com/users/show/341982673'},
#   'review_scores_rating': 20.0,
#   'reviews_per_month': 0.48},
#  {'_id': {'id': 373978025,
#           'name': 'T',
#           'url': 'https://www.airbnb.com/users/show/373978025'},
#   'review_scores_rating': 20.0,
#   'reviews_per_month': 0.43},
#  {'_id': {'id': 175247286,
#           'name': 'Severin Pierre',
#           'url': 'https://www.airbnb.com/users/show/175247286'},
#   'review_scores_rating': 20.0,
#   'reviews_per_month': 0.4},
#  {'_id': {'id': 340857186,
#           'name': 'Max',
#           'url': 'https://www.airbnb.com/users/show/340857186'},
#   'review_scores_rating': 20.0,
#   'reviews_per_month': 0.33}]