import pymongo
import datetime
import re
import csv
import pprint

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["soen363"]

def sanitizeRow(row):
  int_regex = "^-?\d+$"
  float_regex = "^\d+(\.\d*)?$"
  price_regex = "^\$\d+(\.\d*)?$"
  percent_regex = "^\d+\%?$"
  date_regex = "^\d{4}-\d{2}-\d{2}$"
  for col in row:
    # Number
    if re.match(int_regex, row[col]) is not None:
      row[col] = int(row[col])
      continue

    if re.match(float_regex, row[col]) is not None:
      row[col] = float(row[col])
      continue

    # Prices
    if re.match(price_regex, row[col]) is not None:
      row[col] = float(row[col][1:])
      continue
  
    # Percent
    if re.match(percent_regex, row[col]) is not None:
      row[col] = float(row[col][0:len(row[col]) - 1])
      continue

    # Dates
    if re.match(date_regex, row[col]) is not None:
      row[col] = datetime.datetime.strptime(row[col], "%Y-%m-%d")

    # Booleans
    if (row[col] == "t"):
      row[col] = True
      continue
    if (row[col] == "f"):
      row[col] = False

    # Nulls
    if (row[col] == "N/A" or row[col] == ""):
      row[col] = None
      continue
  return row

def loadFile(name, filename):
  col = db[name]
  print(f'Loading {name}... This might take a while...')
  with open(filename, encoding="utf8") as file:
    reader = csv.DictReader(file)
    for row in reader:
      row = sanitizeRow(row)
      col.insert_one(row)
  print(f'Loaded {name} successfully!')

a = datetime.datetime.now()
loadFile('listings', '../extracted_mongo/listings-montreal.csv')
loadFile('listings', '../extracted_mongo/listings-toronto.csv')
loadFile('listings', '../extracted_mongo/listings-quebec.csv')

loadFile('reviews', '../extracted_mongo/reviews-montreal.csv')
loadFile('reviews', '../extracted_mongo/reviews-toronto.csv')
loadFile('reviews', '../extracted_mongo/reviews-quebec.csv')
b = datetime.datetime.now()
c = b - a
pprint.pprint(str(c.microseconds * 0.001) + ' ms')

#loadFile('reviews', '../extracted_mongo/reviews.csv')
#loadFile('calendar', '../extracted_mongo/calendar.csv')