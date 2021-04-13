# Order all neighborhoods by number of listings
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
listings = db["listings"]

pipeline = [
  { "$group": { "_id": "$neighbourhood_cleansed", "sum": { "$sum": 1 } }, },
  { "$sort": { "sum": -1 } }
]

import pprint
pprint.pprint(list(listings.aggregate(pipeline)))

# Results:
# [{'_id': 'Ville-Marie', 'sum': 4069},
#  {'_id': 'Le Plateau-Mont-Royal', 'sum': 3603},
#  {'_id': 'Rosemont-La Petite-Patrie', 'sum': 1270},
#  {'_id': 'Côte-des-Neiges-Notre-Dame-de-Grâce', 'sum': 1041},
#  {'_id': 'Le Sud-Ouest', 'sum': 956},
#  {'_id': 'Mercier-Hochelaga-Maisonneuve', 'sum': 711},
#  {'_id': 'Villeray-Saint-Michel-Parc-Extension', 'sum': 701},
#  {'_id': 'Verdun', 'sum': 321},
#  {'_id': 'Ahuntsic-Cartierville', 'sum': 273},
#  {'_id': 'Saint-Laurent', 'sum': 160},
#  {'_id': 'Outremont', 'sum': 151},
#  {'_id': 'LaSalle', 'sum': 119},
#  {'_id': 'Westmount', 'sum': 97},
#  {'_id': 'Lachine', 'sum': 85},
#  {'_id': 'Montréal-Nord', 'sum': 65},
#  {'_id': 'Saint-Léonard', 'sum': 63},
#  {'_id': 'Rivière-des-Prairies-Pointe-aux-Trembles', 'sum': 63},
#  {'_id': 'Anjou', 'sum': 51},
#  {'_id': 'Côte-Saint-Luc', 'sum': 47},
#  {'_id': 'Pointe-Claire', 'sum': 47},
#  {'_id': 'Pierrefonds-Roxboro', 'sum': 46},
#  {'_id': 'Dollard-des-Ormeaux', 'sum': 38},
#  {'_id': 'Mont-Royal', 'sum': 36},
#  {'_id': 'Dorval', 'sum': 36},
#  {'_id': "L'Île-Bizard-Sainte-Geneviève", 'sum': 19},
#  {'_id': 'Montréal-Ouest', 'sum': 13},
#  {'_id': 'Beaconsfield', 'sum': 11},
#  {'_id': 'Kirkland', 'sum': 8},
#  {'_id': 'Hampstead', 'sum': 8},
#  {'_id': "Baie-d'Urfé", 'sum': 5},
#  {'_id': 'Sainte-Anne-de-Bellevue', 'sum': 3},
#  {'_id': 'Senneville', 'sum': 2},
#  {'_id': 'Montréal-Est', 'sum': 2}]