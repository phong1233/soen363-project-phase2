-- Find a list of countries that were above the global average temperature in 2013
SELECT country, average_temp as max_average_temp
FROM (SELECT country, MAX(average_temp) as average_temp
      FROM globallandtemperaturesbycountry
      WHERE average_temp IS NOT NULL
        AND dt BETWEEN '2013-01-01' and '2013-12-31'
      GROUP BY (country)) as temp
WHERE temp.average_temp IS NOT NULL
  and average_temp >= (
    SELECT MAX(land_avg_temp)
    FROM globaltemperatures
    WHERE dt BETWEEN '2013-01-01' and '2013-12-31'
)
ORDER BY average_temp DESC
LIMIT 10;

-- Result:
-- country              | max_average_temp
-- ----------------------------------------
-- Kuwait               | 38.234 |
-- Qatar                | 37.07  |
-- Bahrain              | 36.922 |
-- United Arab Emirates | 36.696 |
-- Saudi Arabia         | 35.706 |
-- Iraq                 | 35.494 |
-- Algeria              | 34.707 |
-- Mali                 | 34.587 |
-- Djibouti             | 34.532 |
-- Mauritania           | 34.282 |
