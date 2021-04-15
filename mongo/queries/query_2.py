# Find the average listing price per neighbourhood
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]

pipeline = [
  { "$group": { "_id": "$neighbourhood_cleansed", "avg_price": { "$avg": "$price" } }, },
  { "$sort": { "avg_price": -1 } }
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
# [{'_id': "L'Île-Bizard-Sainte-Geneviève", 'avg_price': 192.73684210526315},
#  {'_id': 'Côte-Saint-Luc', 'avg_price': 139.72727272727272},
#  {'_id': 'Kirkland', 'avg_price': 135.875},
#  {'_id': 'Westmount', 'avg_price': 134.57894736842104},
#  {'_id': 'Pierrefonds-Roxboro', 'avg_price': 128.95555555555555},
#  {'_id': 'Beaconsfield', 'avg_price': 128.9090909090909},
#  {'_id': 'Hampstead', 'avg_price': 125.71428571428571},
#  {'_id': 'Dollard-des-Ormeaux', 'avg_price': 116.48648648648648},
#  {'_id': 'Mont-Royal', 'avg_price': 113.25},
#  {'_id': 'Outremont', 'avg_price': 112.1744966442953},
#  {'_id': 'Ville-Marie', 'avg_price': 109.00074404761905},
#  {'_id': "Baie-d'Urfé", 'avg_price': 106.33333333333333},
#  {'_id': 'Le Sud-Ouest', 'avg_price': 103.83227848101266},
#  {'_id': 'Montréal-Ouest', 'avg_price': 103.53846153846153},
#  {'_id': 'Pointe-Claire', 'avg_price': 101.08510638297872},
#  {'_id': 'Le Plateau-Mont-Royal', 'avg_price': 98.47335950644981},
#  {'_id': 'Dorval', 'avg_price': 96.30555555555556},
#  {'_id': 'Saint-Léonard', 'avg_price': 94.38709677419355},
#  {'_id': 'LaSalle', 'avg_price': 92.5798319327731},
#  {'_id': 'Lachine', 'avg_price': 91.83529411764705},
#  {'_id': 'Saint-Laurent', 'avg_price': 89.88679245283019},
#  {'_id': 'Rosemont-La Petite-Patrie', 'avg_price': 85.84281200631912},
#  {'_id': 'Rivière-des-Prairies-Pointe-aux-Trembles',
#   'avg_price': 84.33870967741936},
#  {'_id': 'Côte-des-Neiges-Notre-Dame-de-Grâce', 'avg_price': 83.21511627906976},
#  {'_id': 'Mercier-Hochelaga-Maisonneuve', 'avg_price': 81.88135593220339},
#  {'_id': 'Verdun', 'avg_price': 80.53291536050156},
#  {'_id': 'Montréal-Est', 'avg_price': 80.0},
#  {'_id': 'Anjou', 'avg_price': 77.76470588235294},
#  {'_id': 'Montréal-Nord', 'avg_price': 77.55384615384615},
#  {'_id': 'Villeray-Saint-Michel-Parc-Extension',
#   'avg_price': 77.39571428571429},
#  {'_id': 'Ahuntsic-Cartierville', 'avg_price': 77.14338235294117},
#  {'_id': 'Senneville', 'avg_price': 40.0},
#  {'_id': 'Sainte-Anne-de-Bellevue', 'avg_price': 20.333333333333332}]