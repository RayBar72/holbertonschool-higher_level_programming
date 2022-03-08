-- displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending) limit 3 and ag and jul
SELECT city, avg(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
