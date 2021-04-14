-- Find top 5 state (province and territory) that are above the canada temperature average in 2010
SELECT the_state, state_average_temp, canada_average_temp
FROM (SELECT AVG(average_temp) as canada_average_temp
      FROM globallandtemperaturesbycountry
      WHERE country = 'Canada'
        and dt BETWEEN '2010-01-01' and '2010-12-31') canada_temp,
     (SELECT the_state, AVG(average_temp) as state_average_temp
      FROM globallandtemperaturesbystate
      WHERE country = 'Canada'
        and dt BETWEEN '2010-01-01' and '2010-12-31'
      GROUP BY the_state) state_temp
WHERE state_average_temp >= canada_average_temp
ORDER BY state_average_temp DESC
LIMIT 5;

-- Result:
-- |the_state                |state_average_temp|canada_average_temp|
-- +-------------------------+------------------+-------------------+
-- |Nova Scotia              |8.15524991353353  |-1.8879166555901368|
-- |Prince Edward Island     |7.640333483616511 |-1.8879166555901368|
-- |New Brunswick            |6.753083275941511 |-1.8879166555901368|
-- |Ontario                  |3.119250019391378 |-1.8879166555901368|
-- |Newfoundland And Labrador|1.9753332634766896|-1.8879166555901368|

