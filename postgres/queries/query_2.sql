-- Find the city with the maximum average temperature
SELECT city, dt, average_temp as max_average_temp
FROM globallandtemperaturesbycity
WHERE average_temp IS NOT NULL
  and average_temp = (
    SELECT MAX(average_temp)
    FROM globallandtemperaturesbycity
);

-- Results:
-- City    | dt         | max_average_temp
-- ---------------------------------------
-- Warqla  | 1761-07-01 | 39.651
