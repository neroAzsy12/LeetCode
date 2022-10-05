/*
Table: cinema (id int, movie varchar(255), description varchar(255), rating float(2, 1))

Write an SQL query to report the movies with an odd-numbered ID and a description that is not "boring".
Return the result table ordered by rating in descending order.
*/
SELECT *
FROM cinema
WHERE id % 2 = 1 AND description != 'boring'
ORDER BY rating DESC;