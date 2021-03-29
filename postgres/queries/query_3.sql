-- Find the country with the maximum average temperature from 1800 to 1900
SELECT country, dt, average_temp as max_average_temp
FROM GlobalLandTemperaturesByCountry
WHERE average_temp IS NOT NULL
  and dt BETWEEN '1800-01-01' and '1900-01-01'
  and average_temp = (
    SELECT MAX(average_temp)
    FROM globallandtemperaturesbycountry
    WHERE dt BETWEEN '1800-01-01' and '1900-01-01'
);

-- Result:
-- Country | dt         | max_average_temp
-- ---------------------------------------
-- Kuwait  | 1840-07-01 | 37.261
