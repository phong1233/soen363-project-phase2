-- Find the top 10 country with the highest temperature ever
SELECT country, MAX(average_temp) as max_average_temp
FROM globallandtemperaturesbycountry
WHERE average_temp IS NOT NULL
GROUP BY (country)
ORDER BY max_average_temp DESC
LIMIT 10;

-- Result:
-- | country              | max_average_temp |
-- | -------------------- | ---------------- |
-- | Kuwait               | 38.842           |
-- | United Arab Emirates | 37.75            |
-- | Qatar                | 37.603           |
-- | Bahrain              | 37.471           |
-- | Iraq                 | 37.401           |
-- | Saudi Arabia         | 36.495           |
-- | Algeria              | 35.829           |
-- | Mali                 | 35.33            |
-- | Djibouti             | 35.175           |
-- | Oman                 | 35.096           |
