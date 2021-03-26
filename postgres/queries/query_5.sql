-- Average temperature of Montreal in 2010
SELECT city, AVG(average_temp)
FROM globallandtemperaturesbycity
WHERE city = 'Montreal'
  and average_temp IS NOT NULL
  and dt BETWEEN '2010-01-01' and '2010-12-31'
GROUP BY (city);

-- Result:
-- City     | avg
-- ----------------------------
-- Montreal | 7.114416609207789
