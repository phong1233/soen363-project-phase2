# Find the listing with the highest number of reviews

import pymongo
import pprint
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]


a = datetime.datetime.now()

res = listings.find_one(
    {},
    {
        'number_of_reviews': 1,
        'name': 1,
        'description': 1,
        'neighbourhood_cleansed': 1,
        'host_location': 1
    },
    sort=[("number_of_reviews", -1)])

b = datetime.datetime.now()

c = b - a
pprint.pprint(res)
pprint.pprint(str(c.microseconds * 0.001) + ' ms')

# Result
# {'_id': ObjectId('607f137eb5928748da840393'),
#  'description': 'Flexible check in/out, staying with me in top floor (24 '
#                 'stairs up) 40 year old sunny townhouse complex: 650 square '
#                 'feet electric heating. 8 mins from downtown by 24 hour '
#                 'transit/bike; 25 mins walk). A few small shops/restaurants '
#                 'nearby: sushi, greek, ethiopian, breakfast.  lgbt positive. I '
#                 "cherish guests' suggestions. Corktown neighbourhood is east "
#                 'of downtown, slowly growing, eclectic, working class and '
#                 'safe.<br />Anything you need, just ask!<br /><br /><b>The '
#                 'space</b><br />Welcome to Corktown district in Toronto '
#                 '(Downtown East). Nice, residential street but so close to the '
#                 'action and pulse of the city.<br />Easy key access upon '
#                 'arrival for confirmed guests.<br /><br />Come and share my '
#                 'space in Toronto.   I am a non-smoker.  If you wish to smoke, '
#                 'only outside on the patio/balcony.<br /><br />My calendar is '
#                 'always current, even if it appears as "last update x days '
#                 'ago" which means I most likely have had no changes in that '
#                 'period.<br /><br />Wake up ready to start your day with '
#                 'fresh,',
#  'host_location': 'Toronto, Ontario, Canada',
#  'name': 'SUNNY DBL CORKTOWN BREAKFAST EAST DOWNTOWN',
#  'neighbourhood_cleansed': 'Regent Park',
#  'number_of_reviews': 828}
# '72.996 ms'