-- Find the top 10 country with the lowest temperature ever at any time
SELECT country, MIN(average_temp) as min_temp
FROM globallandtemperaturesbycountry
WHERE average_temp IS NOT NULL
GROUP BY (country)
ORDER BY min_temp
LIMIT 10;

-- Result:
-- |country               |min_temp|
-- +----------------------+--------+
-- |Greenland             |-37.658 |
-- |Denmark               |-36.83  |
-- |Russia                |-30.577 |
-- |Canada                |-28.736 |
-- |Mongolia              |-27.442 |
-- |Kazakhstan            |-23.601 |
-- |Svalbard And Jan Mayen|-22.587 |
-- |Finland               |-21.2   |
-- |Kyrgyzstan            |-19.161 |
-- |Sweden                |-16.608 |


