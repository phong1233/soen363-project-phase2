# Find the most expensive listing that is booked all year


import pymongo
import pprint
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]

fullyBooked = {"availability_365": 0.0}

res = listings.find_one(fullyBooked,  {
    'name': 1,
    'description': 1,
    'neighbourhood_cleansed': 1,
    'host_location': 1,
    'availability_365':1,
    'price':1
}, sort=[("price", -1)])


a = datetime.datetime.now()
b = datetime.datetime.now()

c = b - a
pprint.pprint(res)
pprint.pprint(str(c.microseconds * 0.001) + ' ms')

#Results

# {'_id': ObjectId('6078cabcd891aa9d948701f6'),
#  'availability_365': 0,
#  'description': 'This luxurious Penthouse boasts rich fabrics and textures, '
#                 'leather, wood and steel along with original stone and '
#                 'brickwork. This fully equipped, 3- story loft includes two '
#                 'bedrooms, two bath, two balconies, a fireplace and full '
#                 'kitchen.<br /><br />Registration Number: 603094',
#  'host_location': 'Montreal, Quebec, Canada',
#  'name': 'Hotel Epik Montreal, Penthouse',
#  'neighbourhood_cleansed': 'Ville-Marie',
#  'price': '$7,000.00'}
# '0.0 ms'

