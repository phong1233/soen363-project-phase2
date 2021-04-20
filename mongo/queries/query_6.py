# Find 10 reviews which have "comfortable" in their comments
import pymongo
import pprint
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
reviews = db["reviews"]

pipeline = [
    {"$match":
        {'comments':
             {'$regex': '/.*comfortable.*/', '$options': 'i' }
         }
     },
    { "$group": { "_id": { "id": "$listing_id", "reviewer": "$reviewer_name", "comment": "$comments" }}},
    {"$limit":10}
]

a = datetime.datetime.now()
res = list(reviews.aggregate(pipeline))
b = datetime.datetime.now()

c = b - a
pprint.pprint(res)
pprint.pprint(str(c.microseconds * 0.001) + ' ms')

#Result
# {'_id': {'comment': 'This AirBnb was truly a great experience. Check-in/Out '
#                     'is extremely simple, the apartment itself is very clean, '
#                     'with a well stocked kitchen, and a great location. The '
#                     'beds are comfortable and clean, the floor is quiet, and '
#                     'the apartment is stylish. There is a smart TV which '
#                     'makes it easy to watch Netflix or YouTube, and the '
#                     'washer/dryer are certainly a plus. The amenities in the '
#                     'building are great and the pool and steam rooms were '
#                     'both awesome. Building is safe and secure as it requires '
#                     'a key fob to get in the front. Would very much recommend '
#                     'this AirBnb to potential renters.',
#          'id': 25003790,
#          'reviewer': 'Michael'}},
# {'_id': {'comment': 'This is a cute little bedroom/bathroom inside a hotel. '
#                     'Despite the hotel, generally, being a little run-down, '
#                     'the bedroom itself is clean, refurbished and '
#                     'comfortable, with airconditioning and refrigerated '
#                     'water/coke.\n'
#                     'My only issue with the place was the location. Being a '
#                     'solo traveller, there were a couple of places I would '
#                     'recommend steering clear of, like the park at the end of '
#                     'the street. \n'
#                     'Having said that, it was handy to the metro and the bus '
#                     'station for my tour, so I was happy all in all.',
#          'id': 33931772,
#          'reviewer': 'Kate'}},
# {'_id': {'comment': 'The neighborhood and location of this apartment is '
#                     'perfect for a stay in downtown Montreal. Highly '
#                     'recommend!\n'
#                     '\n'
#                     'The hosts Peter and Karyma made us feel safe and welcome '
#                     'throughout the stay. We met my cousin and her family, '
#                     'and they arrived before us but Peter called us while we '
#                     'were driving to Montreal  to ensure that it was OK to '
#                     'give my cousin the keys and access to the apartment. '
#                     'Peter and Karyma met us upon arrival and before '
#                     'departure - with some croissants and a baguette for the '
#                     'road!\n'
#                     '\n'
#                     'The apartment itself was excellent - very clean, '
#                     'comfortable and with all of the amenities. The central '
#                     'A/C was particularly nice given the summer heat. I will '
#                     'say that the apartment does sleep 6 but it will be most '
#                     'comfortable if your 6 people are three couples - we were '
#                     'one couple, one single, one parent and two children, so '
#                     'the sleeping situation was a little tight. But there is '
#                     'an air mattress included that we elected not to use, '
#                     'which may have improved the sleeping arrangements. As it '
#                     'is, I would say it is most comfortable for 4-5 guests '
#                     "and 6 if you're friendly :) Parking for $10/day is also "
#                     'two blocks away and very convenient.\n'
#                     '\n'
#                     'To summarize: Fantastic apartment, incredible location, '
#                     'lovely hosts, and luxurious accommodations. Highly '
#                     'recommend!',
#          'id': 13250283.0,
#          'reviewer': 'Cameron'}},
# {'_id': {'comment': "Kris's place is in a great downtown location walking "
#                     'distance to many of the major Toronto tourist '
#                     "attractions and with easy access to Toronto's great "
#                     'public transportation.  We arrived by train and left by '
#                     'bus and walked with our suitcases to and from train '
#                     'station and bus depot.  The space is on the 51st floor '
#                     'with a view of the city/lake and a small porch where one '
#                     'can enjoy drinking coffee in the morning sun.  The space '
#                     'is small but efficiently organized and clean. We had '
#                     'never slept in a Murphy bed before and were apprehensive '
#                     'but were amazed how comfortable the mattress was.  Kris '
#                     'met us on arrival.  We arrived in Toronto before '
#                     'check-in time and Kris was gracious in allowing us to '
#                     'leave our bags.  Kris is very quick to respond to '
#                     'texts.   The washer/dryer was a real plus.  Overall, '
#                     'unless you need a lot of space to spread out, this is a '
#                     'great AirB&B from which to explore Toronto.',
#          'id': 24371570,
#          'reviewer': 'Raul'}},
# {'_id': {'comment': 'The location was incredibly central. We were probably a '
#                     '20 minute walk from practically everything, not to '
#                     'mention a 7 minute walk to the metro/bus station and '
#                     'major bank that changes money at a good rate. Guillaume '
#                     'was super quick to email us the info for a shuttle bus '
#                     'that took us directly to the apartment. The place was '
#                     'clean, exactly as pictured, beds were comfortable, A/C '
#                     'super - but buyer beware, their units share the same '
#                     'building with a nightclub. You will hear a wide '
#                     'selection of dance/club music until 3am. We loved it, '
#                     'but early risers may not find this spot suitable.',
#          'id': 18287017.0,
#          'reviewer': 'Sigal'}},
# {'_id': {'comment': 'The house was just perfect. Easy check-in/ check-out. '
#                     'Extremely clean. Quiet neighbourhood. Really comfortable '
#                     'bed. The garden/ terrace is lovely.',
#          'id': 262688.0,
#          'reviewer': 'Maria'}},
# {'_id': {'comment': "Our stay at Driss' place went great. The apartment is "
#                     'roomy, has big windows providing a lot of sunshine and '
#                     'there was ample space for our family of six. Furniture '
#                     'appeared to be new, in great condition and comfortable. '
#                     'Checking in was a breeze with the instructions Driss '
#                     'provided. The apartment is on the second (Website hidden '
#                     'by Airbnb) there is a full flight of steps. The wifi was '
#                     'easy to figure out; signal and range were great. I was '
#                     'able to catch it from outside the home inside my car as '
#                     'well. Parking is not too difficult to find although it '
#                     'took a little effort to translate the signs and figure '
#                     'out if a particular spot was with a time limit or not. '
#                     'Driss also recommended parking on the street next to the '
#                     'restaurant across the street as there is some free '
#                     'parking there as well. My mom, brother and sister each '
#                     'got their own room. My husband and I shared the room '
#                     'with a queen sized bed and a futon. We pulled the futon '
#                     'up to the foot of the bed, still in shape of a sofa, put '
#                     'pillows on two ends and made a perfect sleeping area for '
#                     'our toddler. In the morning she would climb on top of '
#                     'our bed to wake us up for morning cuddles. The '
#                     'sheets/covers were pristine white, clean and beds were '
#                     'very comfortable. The down side to the bedrooms in the '
#                     'front of the apartment was that there was too much '
#                     "sunshine too early in the morning. It wasn't too big of "
#                     'a deal since our toddler wakes up by 8 am anyway but I '
#                     'would recommend putting blackout curtains in those two '
#                     'bedrooms. The kitchen is ideal for an apartment of this '
#                     'size with a top freezer refrigerator and full sized '
#                     'range. We picked up grocery from the grocery store '
#                     '"Metro" just a couple blocks away and had homemade '
#                     'breakfast daily to start our day of exploring. The '
#                     'kitchen has a large window and also leads to the '
#                     'balcony. This was really helpful with ventilation while '
#                     'cooking. While we cooked, my daughter enjoyed spending '
#                     'time on the balcony watching cars go by. There was a '
#                     'clean sponge, dish detergent, enough pots pans and '
#                     'dinnerware. The last guests left a few Nespresso pods to '
#                     'get us hooked, so we went and bought more...and left the '
#                     'remaining to get the next guests hooked! Also, if you '
#                     'buy Maple syrup...get the jar with a vanilla bean stick '
#                     'inside of it...so so good! There was a full sized washer '
#                     'and dryer in the kitchen. We were able to do a load of '
#                     'laundry before the end of our stay and therefore had '
#                     'less work to do when we returned home. Would recommend '
#                     'guests to bring their own detergent and dryer sheets and '
#                     'there were none in the apartment. We picked some up at '
#                     'Metro. The bathroom was clean and well stocked with '
#                     'toilet paper and towels. The shampoo/conditioner/body '
#                     'wash dispenser was an unexpected bonus. We happened '
#                     'to...',
#          'id': 19964276.0,
#          'reviewer': 'Rabia'}},
# {'_id': {'comment': 'Our rental occurred during over a cold week in Dec / '
#                     'Jan, and the suite provide us a warm, comfortable, '
#                     'modern,  fully featured living experience.  We enjoyed '
#                     'the ability to prepare our own breakfast before heading '
#                     'out for the day.  Great location near great shops, '
#                     'restos, and services in Little Italy / Palmerston area.  '
#                     'Would highly recommend the suite, and Arthur was very '
#                     'quick to respond to any questions we had before we ever '
#                     'arrived.  Very comfortable beds as well provided a great '
#                     'nights sleep.  Having the parking space was also a huge '
#                     'plus.',
#          'id': 2997407,
#          'reviewer': 'David'}},
# {'_id': {'comment': 'The apartment was very clean and cozy! Great location in '
#                     'a quiet neighbor hood. It only took us about 10-15min '
#                     'drive to get to downtown Quebec City. Perfect for two '
#                     'people and maybe a third but not a fourth (like '
#                     'advertised) We had my mom and my 2 year old daughter '
#                     'with my husband and myself...there was a futon and '
#                     'single mattress that we set up on the living room floor '
#                     'which did the trick for the night. The futon is not '
#                     'meant for 2 people...when you unfold it it has a very '
#                     'hard/uncomfortable bar in the centre. If this spot had a '
#                     'sofa bed/pull out couch it would make it a great '
#                     'apartment for 4 people.',
#          'id': 14340644,
#          'reviewer': 'Stacia'}},
# {'_id': {'comment': 'Located in the Griffintown area of downtown Montreal, '
#                     'this brand new building is neatly situated with amazing '
#                     'views of the city/Mount Royal, and close proximity to '
#                     'the trendy bars and restaurants of Rue Notre-Dame.  The  '
#                     'apartment has a terrace that was both comfortable and '
#                     'private that can be accessed from all rooms (the city '
#                     'facing wall is nearly all glass).  We used it a lot '
#                     'during our stay.   Everything was perfectly clean and '
#                     'bright.   The kitchen was well appointed with nice '
#                     'touches such as a Nespresso machine, full size fridge, '
#                     'dishwasher and all the utensils you would need to cook '
#                     'meals.   There is also a washer/dryer set right off the '
#                     'kitchen.    The beds and linens were welcoming and very '
#                     'comfortable.   The building also has a gym and an '
#                     'outdoor pool.   The apartment and building were '
#                     'extremely well managed.  Overall this was a terrific '
#                     'stay for us.  Highly recommended.  Be sure to check out '
#                     'the butcher shop on the corner of Rue Richmond and Rue '
#                     'Notre Dame.  They carry some better wine and cheese in '
#                     'additional to a spectacular display of meats.',
#          'id': 35249259.0,
#          'reviewer': 'Justin'}}]
# '276.267 ms'