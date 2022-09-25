/*
Table: World (name varchar(255), continent varchar(255), area int, population int, gdp int)

Write a query to report the name, population, and area of the big countries.
*/
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;