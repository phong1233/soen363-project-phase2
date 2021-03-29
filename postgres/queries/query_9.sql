-- Find top 3 state (province and territory) that are above the canada temperature average
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

-- Result:
-- |the_state                |state_average_temp|canada_average_temp|
-- +-------------------------+------------------+-------------------+
-- |Nova Scotia              |8.15524991353353  |-1.8879166555901368|
-- |Prince Edward Island     |7.640333483616511 |-1.8879166555901368|
-- |New Brunswick            |6.753083275941511 |-1.8879166555901368|
-- |Ontario                  |3.119250019391378 |-1.8879166555901368|
-- |Newfoundland And Labrador|1.9753332634766896|-1.8879166555901368|
-- |British Columbia         |1.6802499492963154|-1.8879166555901368|
-- |Alberta                  |1.5974166095256805|-1.8879166555901368|
-- |Saskatchewan             |1.518166681130727 |-1.8879166555901368|
-- |Manitoba                 |0.4930000305175781|-1.8879166555901368|
