-- Find top 10 canadian city that are above the canada temperature average in 2010
SELECT city, avg(average_temp) as city_average_temp, temp.canada_average_temp
FROM globallandtemperaturesbycity,
     (SELECT AVG(average_temp) as canada_average_temp
      FROM globallandtemperaturesbycountry
      WHERE country = 'Canada'
        and dt BETWEEN '2010-01-01' and '2010-12-31') temp
WHERE country = 'Canada'
  and dt BETWEEN '2010-01-01' and '2010-12-31'
  and average_temp >= temp.canada_average_temp
GROUP BY city, country, temp.canada_average_temp
ORDER BY city_average_temp DESC
LIMIT 10;

-- Result:
-- |city     |city_average_temp |canada_average_temp|
-- +---------+------------------+-------------------+
-- |London   |13.880111138025919|-1.8879166555901368|
-- |Hamilton |13.880111138025919|-1.8879166555901368|
-- |Kingston |13.210555473963419|-1.8879166555901368|
-- |Oshawa   |12.780888795852661|-1.8879166555901368|
-- |Toronto  |12.434333350923326|-1.8879166555901368|
-- |Waterloo |12.434333350923326|-1.8879166555901368|
-- |Guelph   |12.434333350923326|-1.8879166555901368|
-- |Barrie   |12.434333350923326|-1.8879166555901368|
-- |Kitchener|12.434333350923326|-1.8879166555901368|
-- |Quebec   |11.858571461268834|-1.8879166555901368|

