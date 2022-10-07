/*
Table: Departments (id int, name varchar(30))
Table: Students (id int, name varchar(30), department_id int)

Write an SQL query to find the id and the name of all students who are enrolled in departments that no longer exist.
Return the result table in any order.
*/
-- Solution #1
SELECT Students.id, Students.name
FROM Students
LEFT JOIN Departments
ON Students.department_id = Departments.id
WHERE Departments.id IS NULL;

-- Solution #2
SELECT id, name
FROM Students
WHERE department_id NOT IN (SELECT id from Departments);