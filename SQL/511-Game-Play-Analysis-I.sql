/*
Table: Activity (player_id int, device_id int, event_date date, games_played int)

Write an SQL query to report the first login date for each player.
Return the result table in any order.
*/
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;