# Find the most expensive listing
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]

import pprint
import datetime
a = datetime.datetime.now()
res = res = listings.find_one(
  {},
  {
    'price': 1,
    'name': 1,
    'description': 1,
    'listing_url': 1
  },
  sort=[("price", -1)])
b = datetime.datetime.now()

c = b - a
pprint.pprint(res)
pprint.pprint(str(c.microseconds * 0.001) + ' ms')

# Results:
# {'_id': ObjectId('607f138eb5928748da844542'),
#  'description': 'Situé dans le Vieux Port et jouxtant le Quartier Petit '
#                 'Champlain, au cœur du Vieux Québec, l’Auberge Saint-Antoine '
#                 'est bien plus qu’un simple hôtel. Propriété familiale et '
#                 'icône de la ville de Québec depuis le 18ième siècle, notre '
#                 'établissement est l’union parfaite entre histoire et '
#                 'hospitalité, luxe et commodité,  élégance intemporelle et '
#                 'confort contemporain.<br /><br /><b>The space</b><br />The '
#                 'Suites feature a bedroom with either a Queen or King size '
#                 'bed, a living room area with a sofa bed, and a bathroom with '
#                 'heated flooring and a deep-soaking tub separated shower. They '
#                 'are equipped with a mini bar, a Bose stereo system, a safe, a '
#                 'tea kettle and a Nespresso coffee maker, hob, microwave, oven '
#                 'toaster<br /><br /><b>Guest access</b><br />In addition to '
#                 'its place as a landmark hotel in Québec City, Auberge '
#                 'Saint-Antoine is renowned for its impeccable amenities, '
#                 'modern features, and distinctive service that caters to even '
#                 'the most discerning guest. Enjoy luxurious in-room amenities '
#                 'suc',
#  'listing_url': 'https://www.airbnb.com/rooms/30851050',
#  'name': 'Family Suite',
#  'price': '$9,999.00'}
# '57.0 ms'

# With indexes:
# '16.011 ms'