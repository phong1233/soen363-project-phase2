import pymongo
import datetime
import pprint


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]
reviews = db["reviews"]

a = datetime.datetime.now()

# listings indexes
listings.create_index('neighbourhood_cleansed')
listings.create_index('price')
listings.create_index('listings')
listings.create_index('host_id')
listings.create_index('host_name')
listings.create_index('url')
listings.create_index('review_scores_rating')
listings.create_index('reviews_per_month')
listings.create_index('room_type')

reviews.create_index('listing_id')
reviews.create_index('reviewer_name')

b = datetime.datetime.now()

c = b - a
print('Index created')
pprint.pprint(str(c.microseconds * 0.001) + ' ms')
