/*
Table: Courses (student varchar(255), class varchar(255))

Write an SQL query to report all the classes that have at least five students.
Return the result table in any order.
*/
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;