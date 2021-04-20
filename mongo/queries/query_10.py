# Find 10 reviews which have "dirty" in their reviews
import pymongo
import pprint
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["soen363"]
reviews = db["reviews"]

pipeline = [
    {"$match":
         {'comments':
              {'$regex': '/.*dirty.*/', '$options': 'i' }
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

#Results
# [{'_id': {'comment': 'I would not recommend one to stay here if they want a '
#                      'quiet/clean/comfortable stay. This was honestly the '
#                      'worst airbnb experience I have had. To begin with, it '
#                      'was not made clear that I would be sharing the house '
#                      'with another 4 (or more- not entirely sure) students and '
#                      'midway through the stay, it was mentioned that there '
#                      'would be 8. Additionally, the general cleaniness of the '
#                      'place was lacking and this could be noticed from the '
#                      'odour that permeated. There would be bits of food from '
#                      "the previous day's meals on the dining table, and "
#                      'occasionally dirty dishes would be left in the sink. '
#                      'There is a kitchen advertised in the listing but the '
#                      'pots and pans provided are basically unusable. They are '
#                      'incredibly scratched and old, with one of the handles '
#                      'close to falling off. As for the bathroom, there are a '
#                      'number of rules you should know about- if you need to '
#                      'leave the house early, you might need to have a schedule '
#                      'worked out with Ernesto (and be sure to arrange that '
#                      'with him absolutely 24h before you need it done). The '
#                      'total time you can spend then would be 15min in the '
#                      'toilet, with the shower time capped at 5 min. Other '
#                      'things that were noticeable in the bathroom (but '
#                      'thankfully have changed): there was no mat provided, no '
#                      'soap/shampoo despite essentials being advertised to be '
#                      'provided, and absolutely nowhere to hang anything when '
#                      'you take a shower (towel, clothes etc). No wastepaper '
#                      'basket provided in the room or the toilet either, so one '
#                      'of the female students voiced that she had nowhere to '
#                      'throw her sanitary pads and would have to bring them '
#                      'into her room. \n'
#                      '\n'
#                      'Credit goes to Ernesto for having listened to the '
#                      'feedback provided and he did make the effort to quickly '
#                      'make changes especially in the bathroom (there is now a '
#                      'mat, dustbin and a rack to hang clothes/towels). He also '
#                      'was keen to find out how we liked the stay and asked for '
#                      'more feedback. We stayed for a total of 2 weeks and '
#                      'after these changes in the second week, it was better. '
#                      'It must be said however, that this came after a nasty '
#                      'bust up in which he made slights on our integrity and '
#                      'himself made some false claims. It was overall an '
#                      'unpleasant experience and I hope I would never have to '
#                      'stay here again.',
#           'id': 17680070,
#           'reviewer': 'Daniel'}},
#  {'_id': {'comment': 'Great location and condo itself! However VERY dusty and '
#                      'kitchenware/dishes/utensils were dirty. pots and pans '
#                      'were barely useable unless a ton of oil was used and '
#                      'even then food stuck. A/C vents and bathroom fan were '
#                      'full of dust, as was the top of the fridge. \n'
#                      "TV also didn't work although it was stated that Netflix "
#                      'was provided.\n'
#                      'All in all condo has great potential but needs a lot '
#                      'more upkeep to make it a pleasant stay.',
#           'id': 21839092,
#           'reviewer': 'Ayesha'}},
#  {'_id': {'comment': 'Great location, easy check in and quick responses, '
#                      'however a few items led to low rating: visibly broken '
#                      'mattress/box spring as bed caves in, duvet cover had '
#                      'stains, dishwasher with dirty smelly dishes was not run, '
#                      'and would be nice to have a microwave. With few '
#                      'changes/fixes place would be a 5 star',
#           'id': 20984414,
#           'reviewer': 'Jin'}},
#  {'_id': {'comment': 'PROs: Beautifully designed. Comfy bed. Amazing view. '
#                      'Great indoor hot tub, fairly private. Prompt replies '
#                      'from host. Clear check-in & parking instructions. \n'
#                      '\n'
#                      'CONs: Fireplace non-functioning. Several items broken/ '
#                      'missing/ unstocked. Windows dirty. Mentioned issues to '
#                      'host and he was very apologetic, will follow up with his '
#                      'cleaning/maintenance staff. \n'
#                      '\n'
#                      'Overall, a positive experience!',
#           'id': 29480423,
#           'reviewer': 'Julie'}},
#  {'_id': {'comment': 'Great location! The space was good for a group of 6. '
#                      'Unfortunately we were very disappointed with the '
#                      'cleanliness of this place. Did not feel comfortable with '
#                      'using the towels/dishes/sheets as almost everything was '
#                      'dirty/had stains.',
#           'id': 33887055,
#           'reviewer': 'Behshad'}},
#  {'_id': {'comment': 'A good spot for a single person or a couple to stay but '
#                      'I wouldn’t suggest 3 people or more. The space is a '
#                      'little smaller than what I expected based off the '
#                      'pictures but still manageable for a short period of '
#                      'time. I personally found the sofa bed to be really hard '
#                      'and uncomfortable but you can’t expect much comfort from '
#                      'sofa beds in general. Frank supplied extra linen and '
#                      'towels and the kitchen was stocked with utensils and '
#                      'plates/bowls which was nice of him to do. Check in and '
#                      'out was easy and the padlock code door made it easy to '
#                      'go in and out without having to worry about a key. As '
#                      'mentioned, the subway is conveniently steps away from '
#                      'the home but that comes with a cost of hearing loud '
#                      'rumbling from the passing trains all night. We got used '
#                      'to it after awhile but it could be annoying for someone '
#                      'who is a light sleeper. The only complaint I have is the '
#                      'cleanliness of the bedroom. Upon entering, we '
#                      'immediately noticed how dirty the rug was in the '
#                      'bedroom, it was filled with lint/hair which was a little '
#                      'disgusting. We also noticed large very visible dust '
#                      'accumulations on the baseboard of the wall next to the '
#                      'bed. Aside from all of that, it’s a nice convenient '
#                      'location and Frank was accommodating and made our trip '
#                      'easy and stress free.',
#           'id': 24411312,
#           'reviewer': 'Sophie'}},
#  {'_id': {'comment': 'The host was very quick to respond to communications and '
#                      'fixed an issue that came up right away. The place itself '
#                      'was roomy enough for us and had everything we needed. '
#                      'Electrical is very spotty, kitchen light and some '
#                      'outlets do not work. Walking into the apartment I felt '
#                      'caught off guard compared to what I expected from the '
#                      'photos. It was quite dingy/dirty/run down kind of place.',
#           'id': 37055649,
#           'reviewer': 'Cristina'}},
#  {'_id': {'comment': 'Very uncomfortable/regrettable stay.  This, in fact, is '
#                      '1/2 of a basement on the 1/2 ground level. While the '
#                      'interior of the spaces matches the photos, what was not '
#                      'shown is the path that you have to walk thru to get to '
#                      'your basement apt entrance. After spending 10-15 min '
#                      'searching for a parking spot every night, you walk into '
#                      'a dark alley (about 10m), with smelly garbage dumped on '
#                      'both side of the alley. At / end of alley, turn left and '
#                      'you walk into 2 cars semi blocking the entrance to the '
#                      'basement units. There are woods and other dumps and '
#                      'garbage in the vicinity. There are spider webs that you '
#                      'will walk right into your face. You will have to squeeze '
#                      'thru 2 vehicles w/o dirtying your clothes before you get '
#                      'to  Ft dr #1. Unlock  dr #1, you walk into an unfinished '
#                      'hallway w/ woods piling in front of dr #2, which open '
#                      'into the basement apt. Imagine if you are dressed in '
#                      'some nice clothes, walking thru the above 3-4 times a '
#                      'day from the apt to yr car.  The place is very '
#                      'uncomfortable for following facts. 1. There is no '
#                      'bedboard, so you cannot sit up & read in bed. 2. The '
#                      'humidity in the unit is extremely high. There is a '
#                      'Dehumidifier put away in a small closet room, but we '
#                      'were not informed until we found it on the 2nd night. '
#                      'When i say extremely high, I meant you cannot even sit '
#                      'in the room w/o sweating. We use the dehumidifier (did '
#                      'not help much), and every 10 hrs or so, we need to empty '
#                      'a tank of water fr the dehumidifier tank before it '
#                      'overflows. 3. The outdoor temp at night after 9 pm '
#                      'during our stays (Aug 29-Sept 4) is < 20c. But the '
#                      'inside temp is at 28c. With the humidity and heat, we '
#                      'did not sleep for > 4 hrs per night. 4. On the 4th '
#                      'night, we found a fan (dusty and semi-working) in the '
#                      'closet room. It did little help after we have to wash '
#                      'off the dust on the fan. 5. We inform Ian that we are '
#                      'very uncomfortable & his reply was to buy a fan valued '
#                      'up to $40 and he will refund.  My message to Ian: Hi '
#                      'Ian. We are three nights into our stay and each night '
#                      'has been very uncomfortable. Even last night at 3am it '
#                      'was 28.5^C. Too warm, humid and hard to breathe. As we '
#                      'aren’t even able to open a window. Outside was under 20C '
#                      'Is there anything you can do to make or stay more '
#                      'tolerable. In addition to the comfortability issues, I '
#                      'also wanted to note a few things that are broken: The '
#                      'dryer handle The coffee machine ---------- Ian reply : '
#                      'Hello, maybe you can buy a fan up to 40$ that I would '
#                      'refund you? I have photos, videos to support my claim. '
#                      'Message me on F/b if anyone want to see.',
#           'id': 20071164,
#           'reviewer': 'Robert'}},
#  {'_id': {'comment': 'A regular guest who lives there tried to open my door '
#                      'repeatedly (and aggressively) at three in the morning. '
#                      'As well, there was noise from music and chatting at 8 '
#                      'a.m. thru till 3 / 4 a.m. on all three weekday nights I '
#                      'stayed there. The smell of weed was also pervasive to '
#                      'the point where I had to seek laundry and dry cleaning '
#                      'to maintain professionalism for work (since my clothes '
#                      'smelled strongly when I walked out). \n'
#                      '\n'
#                      "Because of the door situation, I wouldn't recommend this "
#                      'venue to those who are travelling alone and/or for a '
#                      'work trip. I felt very unsafe and threatened. Thankfully '
#                      'JJ was on site and intervened when issues arose, and he '
#                      'also ensured my safety. Appreciated the cleanliness of '
#                      'the bed but was unable to use the kitchenware or fridge '
#                      'as it was quite dirty (there were old tea bags inside '
#                      'the tea kettle that was for shared/common use).  \n'
#                      '\n'
#                      'JJ was a great host, but my experience was unpleasant '
#                      'for the entirety of the four days I stayed there. I felt '
#                      'so unsafe on the last night that I checked out at 6 a.m. '
#                      'on the first train the next morning. Would not stay here '
#                      'again.',
#           'id': 17175506,
#           'reviewer': 'Shazia'}},
#  {'_id': {'comment': 'This is in a great location and very easy to get around '
#                      'via buses/metro. The apartment floor was dirty when we '
#                      'arrived but France was very responsive and kind and had '
#                      'it seen too. You go through a door from the street with '
#                      'a lock, the upstairs and there are two other apartments '
#                      'doors near yours. Note the apartment door is a simple '
#                      'frosted glass door with a simple lock (like a bathroom '
#                      'or bedroom in a home might have). Noise and smells (like '
#                      'smoke) travel through from the stairs/hall a bit and the '
#                      "apartment door doesn't have a deadbolt, something to be "
#                      "aware of if you're funny about locks/people noise.",
#           'id': 744424,
#           'reviewer': 'Eliza'}}]
# '815.778 ms'