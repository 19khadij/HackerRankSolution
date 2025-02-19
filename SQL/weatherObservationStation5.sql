-- (select city, length(city) as name_length from station order by city asc, length(city) asc limit 1)
-- union all
-- (select city, length(city) as name_length from station order by length(city) desc ,city asc  limit 1)

(SELECT CITY, LENGTH(CITY) AS NAME_LENGTH 
 FROM (SELECT CITY FROM STATION ORDER BY LENGTH(CITY) ASC, CITY ASC LIMIT 1) AS Shortest)

UNION ALL

(SELECT CITY, LENGTH(CITY) AS NAME_LENGTH 
 FROM (SELECT CITY FROM STATION ORDER BY LENGTH(CITY) DESC, CITY ASC LIMIT 1) AS Longest);
