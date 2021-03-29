-- Find the country with the maximum average temperature at any time
SELECT country, dt, average_temp as max_average_temp
FROM GlobalLandTemperaturesByCountry
WHERE average_temp IS NOT NULL
  and average_temp = (
    SELECT MAX(average_temp)
    FROM globallandtemperaturesbycountry
);

-- Results:
-- Country | dt         | max_average_temp
-- ---------------------------------------
-- Kuwait  | 2012-07-01 | 38.842
