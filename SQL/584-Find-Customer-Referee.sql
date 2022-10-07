/*
Table: Customer (id int, name varchar(25), referee_id int)

Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
Return the result table in any order.
*/
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;