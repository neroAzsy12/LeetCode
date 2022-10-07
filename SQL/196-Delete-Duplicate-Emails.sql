/*
Table: Person (Id int, Email varchar(255))

Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. 
Note that you are supposed to write a DELETE statement and not a SELECT one.
*/
DELETE p1 FROM Person AS p1
INNER JOIN Person AS p2
ON p1.email = p2.email
WHERE p1.id > p2.id;

DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id > p2.id;