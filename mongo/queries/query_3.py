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
# {'_id': ObjectId('6075f1fa2180f1fa7aa9f4b5'),
#  'description': 'Charmante maison de 3 chambres à coucher, avec un grand '
#                 'espace ouvert salon - salle à manger - cuisine, et d’une cour '
#                 'privée.<br />Située au cœur de Plateau Mont Royal, au coin de '
#                 'l’avenue Mont Royal et à 5min à pied du métro, au pied des '
#                 'cafés et commerces et à 10min à pied du Parc Lafontaine.<br '
#                 '/><br /><b>The space</b><br />Nous habitons notre jolie '
#                 'maison avec nos 2 enfants, et nous la mettons à disposition '
#                 'pendant nos voyages.<br />Elle a 3 chambres confortables, une '
#                 'grande cuisine équipée, un bain avec jacuzzi, un salon avec '
#                 'TV, internet et Netflix. <br />Nous pouvons mettre à '
#                 'disponible les équipements bébé si besoin.<br />Elle est '
#                 'située à un emplacement idéal dans le quartier du Plateau, à '
#                 'proximité des commerces, cafés, restaurants et parcs.<br />Le '
#                 'stationnement est facile dans la rue où les rues '
#                 'parallèles.<br /><br /><b>Guest access</b><br />L’ensemble de '
#                 'la maison est disponible pour les voyageurs. La maison a une '
#                 'terrasse privée et un balcon au 2e étage. <br />Les effets',
#  'listing_url': 'https://www.airbnb.com/rooms/41646280',
#  'name': 'Charmante maison au cœur du Plateau Mont Royal',
#  'price': '$7,000.00'}