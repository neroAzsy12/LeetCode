/*
Table: Employees (id int, name varchar(20))
Table: EmployeeUNI (id int, unique_id int)

Write an SQL query to show the unique ID of each user
If a user does not have a unique ID replace just show null.

Return the result table in any order.
*/
SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI
ON EmployeeUNI.id = Employees.id;