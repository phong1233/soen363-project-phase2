import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]

# listings indexes
listings.create_index('neighbourhood_cleansed')
listings.create_index('price')
listings.create_index('listings')
listings.create_index('host_id')
listings.create_index('host_name')
listings.create_index('url')
listings.create_index('review_scores_rating')
listings.create_index('reviews_per_month')


print('Index created')