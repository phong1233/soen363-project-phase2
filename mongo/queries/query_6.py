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
# [{'_id': {'comment': "We had such a wonderful stay at Derrick's apartment. My "
#                      'husband, myself, and a colleague were in town for a '
#                      'conference at the nearby Chelsea Hotel and had trouble '
#                      'finding reasonable apartments with more than one '
#                      "bedroom. We completely lucked out by finding Derrick's "
#                      'listing and it was perfect for our needs. Two large '
#                      'bedrooms (and big beds!) with two bathrooms, an equipped '
#                      'kitchen, and a great balcony/view. The internet was '
#                      'fast, the building was safe and quiet (with a '
#                      'concierge), and there was free PARKING!! The apartment '
#                      'is also excellently located, close to the subway, '
#                      'directly above a starbucks, and next to two INCREDIBLE '
#                      'restauarants, which I highly recommend:  Bombay Street '
#                      'Food and the Green Grotto. Derrick himself was an '
#                      'excellent host; he went above and beyond to make our '
#                      'stay comfortable. He was quick to respond to all '
#                      'inquiries, was flexible with our stay, and even helped '
#                      'print some documents we needed at the last minute (late '
#                      'at night, no less!). Check-in/out was simple and the '
#                      'detailed instructions he provided were clear and '
#                      'helpful. I highly recommend Derrick and this apartment '
#                      'and I will definitely return next time I am visiting '
#                      'Toronto.',
#           'id': 10299546,
#           'reviewer': 'Andrew And Heather'}},
#  {'_id': {'comment': 'We had a good stay at Kamas place. The house was clean, '
#                      'had the basics of what we needed and such a bonus to '
#                      'have free parking (out front in the day, around back '
#                      'overnight), laundry and AC. Check in and communication '
#                      'were great. The place was very quiet and comfortable and '
#                      'we didn’t know much about the neighbourhood but it was '
#                      'great - resteraunts, cafes, shops and a great brewery '
#                      '“bandit brewery” all within a short walk. Because it is '
#                      'isn’t obvious in the ad, I will explain that most of the '
#                      'living space is on the second floor. On the main floor '
#                      'is an entry/closed in porch and a living room (without a '
#                      'tv), that is also intended for use as a third bedroom '
#                      'with a futon couch. Upstairs are the other 2 bedrooms '
#                      '(spacious, with comfortable beds), a bathroom and a '
#                      'eat-in kitchen with an office/bar off of it. The tv is '
#                      'located in the master bedroom on the second floor. '
#                      'Unfortunately, our toddler knocked over and broke the '
#                      'tv. Kama was extremely understanding of the situation. '
#                      'We left money to reemburse. All around, we had a good '
#                      'stay and this place is great value for the money. I '
#                      'would not recommend the rental to families with moving '
#                      'babies or toddlers but would DEFINITELY recommend to all '
#                      'others. Thanks Kama for a great stay!',
#           'id': 24947265,
#           'reviewer': 'Jessa'}},
#  {'_id': {'comment': 'There are so many fabulous things to say about this '
#                      'beautiful flat it’s hard to know where to begin. Because '
#                      'it’s located on the second floor, you’re afforded '
#                      'somewhat of a treehouse feeling. We loved sitting on the '
#                      'front or back balconies enjoying coffee, a meal, or '
#                      'simply the birdsong coming from the healthy, '
#                      'green-leafed trees. As noted in the listing, plentiful '
#                      'sunlight flows from front to back making the flat glow. '
#                      'Open the doors and you’ll be rewarded with a glorious '
#                      'breeze and a feeling of being outside when you are in. '
#                      'Close the doors and/or windows and the double pane glass '
#                      'shuts out any outdoor sounds. The bed is super '
#                      'comfortable and we loved being able to walk around it to '
#                      'make it up in the morning. The appliances are excellent: '
#                      'a dishwasher that works like a charm, the washer and '
#                      'dryer do an outstanding job, and we loved the huge '
#                      'fridge and perfect stovetop/oven. The kitchen was well '
#                      'equipped with everything and more that you need to pull '
#                      'off a big dinner or a casual bite from heavy cookware, '
#                      'to stainless steel nesting bowls, small appliances, '
#                      'matching plates, bowls, glasses, cups and more. There’s '
#                      'a big flat screen with cable TV and hot, hot, hot Wi-Fi '
#                      'that was fast and omni-present throughout the entire '
#                      'flat. The air conditioner was not often needed but did a '
#                      'great job when called upon. The shower was roomy with '
#                      'great water pressure and ample hot water. The apartment '
#                      'is in easy walking distance to many wonderful places and '
#                      'we found it to be very safe, even late at night. Pickup '
#                      'the green line at the LaSalle Metro station just a few '
#                      'blocks away and in no time you’ll be in the heart of '
#                      'Montreal. A few blocks in another direction you’ll find '
#                      'yourself on the fabled Wellington Street chock full of '
#                      'shops, restaurants, coffee, books, and one of the city’s '
#                      'best fromageries. Visit one of our favs, The Garage Cafe '
#                      'on Hickson Street. A few more minutes from Wellington '
#                      'and you’ll be at a long and lovely string of greenspaces '
#                      'along the St Lawrence River. There you can bike, walk, '
#                      'picnic, or people watch. About a 15-minute walk in yet '
#                      'another direction leads to the Lachine Canal, it’s '
#                      'amazing trail to town, and the historic Atwater Market '
#                      'full of produce, plants, and specialty food shops. '
#                      'Lastly, our host Joanna and her team were the best, fast '
#                      'to communicate and assist with any needs we had. You '
#                      'could tell that the guest experience was absolutely '
#                      'top-of-mind and they were such a pleasure to work with '
#                      'from start to finish. Thank you Joanna, Joel, and '
#                      'Catalina. Our stay at your spotlessly clean Stylish '
#                      'Apartment Near Metro and Services was a joy. I highly '
#                      'recommend your flat to anyone looking to experience all '
#                      'the beauty that Montreal has to offer.',
#           'id': 2083165,
#           'reviewer': 'Evanne'}},
#  {'_id': {'comment': 'Stayed 3 nights 8/24-8/27; Martin communicated well with '
#                      'me before and when I got to his place in order to '
#                      'prepared for my arrival. (Shower towel, wash clothes, '
#                      'wi-fi codes, key). I had very good sleep, bed was '
#                      'comfortable, apartment unit in good location to travel '
#                      'to Old Quebec (25 minutes one way no transfer) and many '
#                      'other places. The only thing I dislike was when upstairs '
#                      'unit residents walking around late night/early morning, '
#                      "could hear it loudly, but that's how the whole "
#                      'residential are. Overall, very good place to stay for a '
#                      'good reasonable price! ',
#           'id': 10829594,
#           'reviewer': 'Simon'}},
#  {'_id': {'comment': 'Spent a lovely weekend in this sunny/brightly lit '
#                      'apartment. Great location near all amenities. Very clean '
#                      '(spotless!), stylish decor (paintings, pillows, plants, '
#                      'furniture - such taste!) and we felt very comfortable '
#                      'using the space as our own. Nice sized balcony with '
#                      'chairs, plants and pillows where we spent one morning '
#                      'reading and tanning (in November!). Told us we could use '
#                      "whatever was in the apt. We couldn't believe how "
#                      'soundproof the apt was! (barely heard the neighbours '
#                      'above) Communication was easy with Michael and his '
#                      'sister (she left the keys/prepared the apt for us '
#                      'because Michael was away). They both replied quickly to '
#                      "our questions. Can't recommend this place enough! Will "
#                      'be back for sure!',
#           'id': 959676,
#           'reviewer': 'Janelle'}},
#  {'_id': {'comment': 'Be warned - if you have more than 3 guests, you are '
#                      'paying a lot of extra for this place, and it’s '
#                      'definitely not worth it. \n'
#                      '\n'
#                      'The third bedroom (the one with the bunk beds) is open '
#                      'to the living room, making it very useless when you have '
#                      'kids you want to put down to bed early. The second '
#                      'bedroom is only accessible through this bunk bed room. \n'
#                      '\n'
#                      'The place is very small, in the basement, has a bad '
#                      'odour that is «\xa0covered up\xa0» with Air Wick '
#                      'lavender room fresheners (if you’re ok with the chemical '
#                      'smell). There’s a lot of mold in the bathroom behind the '
#                      'toilet. \n'
#                      '\n'
#                      'The kitchen is mal equipped, only 3 butter knives, no '
#                      'paper towels, no garbage bags, no dish cloths (I ended '
#                      'up using a wash cloth to do the dishes and our garbage '
#                      'piled way up). \n'
#                      '\n'
#                      'The beds are ridiculously uncomfortable, especially the '
#                      'bunk bed (and the sofa bed, but that’s to be expected, I '
#                      'think). \n'
#                      '\n'
#                      'Because the price breakdown isn’t easily shown, we ended '
#                      'up paying a lot more for this place than it’s worth. At '
#                      'less than $100/night, you expect something that might '
#                      'not be super clean, a little uncomfortable. But at over '
#                      '$200/night, you expect value, to which there was none. \n'
#                      '\n'
#                      'We ended up cancelling our reservation after the first '
#                      'night since we had headaches from the smell and we all '
#                      'had sore backs from the beds. It wasn’t what we expected '
#                      'at all, quite disappointed. It’s the first time I’ve had '
#                      'a bad Airbnb experience. \n'
#                      '\n'
#                      'The host also didn’t answer a question I had asked the '
#                      'day before check in, which might have impacted our stay '
#                      '(we might have cancelled beforehand). \n'
#                      '\n'
#                      'Be aware, there is no air conditioning, it’s very small, '
#                      'the driveway is hard to maneuver (no room to open doors '
#                      'wide, unless you move all the way over on one side and '
#                      'render one side useless). \n'
#                      '\n'
#                      'I’m shocked at the positive reviews, especially since '
#                      'that’s what made me choose this place, but I’m thinking '
#                      'they must have paid less than $100/night for this place. '
#                      'I hope so, at least!',
#           'id': 14357839,
#           'reviewer': 'Linda'}},
#  {'_id': {'comment': "Olga's place is absolutely stunning and has a "
#                      'breathtaking view, especially at night! She was a '
#                      'wonderful host and made me feel very welcome! Checking '
#                      'in/out was so easy and she responded back to any '
#                      'questions right away. The place was super clean, '
#                      'comfortable, and had absolutely everything I was looking '
#                      'for. She even left a booklet of coupons to use around '
#                      'the city which I took advantage of. This was the best '
#                      'location right downtown and within walking distance to '
#                      'many restaurants/bars and shops. Overall, it was a very '
#                      "positive experience and I'd love to stay here again! "
#                      'Thanks Olga!',
#           'id': 13605154,
#           'reviewer': 'Leanne'}},
#  {'_id': {'comment': "I stayed at Shauna's condo for a couple of days after "
#                      'Christmas. The check in/out processes were easy to '
#                      'follow. The space were very clean and provided all the '
#                      'amenities needed, bed was comfortable, and '
#                      "location/value were excellent. Though I didn't get the "
#                      'chance to meet Shauna in person, she was always easy to '
#                      'reach and checked in with me during my stay. Wonderful '
#                      'host and great place - would highly recommend!',
#           'id': 16113662,
#           'reviewer': 'Melissa'}},
#  {'_id': {'comment': 'The listing is extremely accurate, if not an '
#                      "under-representation of how nice an apartment. It's "
#                      'located on the second floor of a small side street only '
#                      "1-2 blocks from Old Montreal's cafes, shops, the port, "
#                      'and Metro access and 3-4 blocks from the convention '
#                      'center. The entryway is up a curved stairwell so be '
#                      'prepared for stairs and to carry your luggage. The rooms '
#                      'are spacious, clean, well-decorated. The kitchen is well '
#                      'stocked, and Tiziano gave great directions when we '
#                      'checked in with help orientating us to the neighborhood '
#                      'and basic layout of the apartment. The beds were '
#                      'clean/comfortable. Bathroom was beautifully renovated. '
#                      'Washer and dryer conveniently in the unit with '
#                      'detergent. The porch off the back had a quiet seating '
#                      'area overlooking the garden. It was quiet at night '
#                      'without a lot of traffic, but easy walking distance from '
#                      'a good portion of the tourist attractions and convention '
#                      'center for business. It was also an easy walk to several '
#                      'bars/restaurants in Centre-Ville, but more of 20-30min '
#                      'walk (1 to 1.5mi). We had a great time for our trip and '
#                      "wouldn't hesitate to recommend this to other "
#                      'friends/travelers. ',
#           'id': 5319105,
#           'reviewer': 'Tina'}},
#  {'_id': {'comment': 'The host was gracious upon arrival and explained in '
#                      'detail the place, location, suggestions for food '
#                      'shopping. The flat is spacious and mostly as pictured. '
#                      'The host replied to questions promptly. The place is not '
#                      'what we expected for the price: the flat was dingy, and '
#                      'with limited supplies in the kitchen - I had to buy '
#                      'kitchen towels, and paper dishes/utensils and soap for '
#                      'the bathroom. There was an issue with the host '
#                      'attempting to enter to the apartment at 10.30pm one day '
#                      'without notice: he tried to enter with his key but we '
#                      "didn't let him open. We were very uncomfortable. I "
#                      'called the next morning to find out what happened and he '
#                      'indicated he thought i had requested help to fix a '
#                      "toilet. However, he didn't call/text to let me know he "
#                      'was coming, nor to apologize for attempting to enter '
#                      'afterwards. He indicated that there was a '
#                      'misunderstanding with another flat. Still, this '
#                      'miscommunication made me feel uncomfortable the rest of '
#                      'my stay. ',
#           'id': 12866623,
#           'reviewer': 'Carolina'}}]
# '244.03300000000002 ms'