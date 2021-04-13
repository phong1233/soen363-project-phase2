-- For the 10 countries with the highest temperature, find the city that has the highest temperature in 2010
SELECT country, city, max(average_temp) as highest_temp
FROM globallandtemperaturesbycity
WHERE country in (
    SELECT country
    FROM globallandtemperaturesbycountry as g3
    WHERE dt BETWEEN '2010-01-01' and '2010-12-31' and average_temp is not null
    GROUP BY country
    ORDER BY max(average_temp) desc
    limit 10
)
and dt BETWEEN '2010-01-01' and '2010-12-31' and average_temp is not null
GROUP BY city, country
ORDER BY max(average_temp) desc
LIMIT 1

-- Result:
-- |country               |city    | highest_temp
-- +----------------------+--------+-------------
-- |Iraq                  |Baghad  |37.899
