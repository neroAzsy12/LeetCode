/*
Table: Users (id int, name varchar(30))
Table: Rides (id int, user_id int, distance int)

Write an SQL query to report the distance traveled by each user.
Return the result table ordered by travelled_distance in descending order, 
if two or more users traveled the same distance, order them by their name in ascending order.
*/
SELECT Users.name, IFNULL(SUM(Rides.distance), 0) AS travelled_distance
FROM Users
LEFT JOIN Rides
ON Users.id = Rides.user_id
GROUP BY Users.id
ORDER BY travelled_distance DESC, Users.name;