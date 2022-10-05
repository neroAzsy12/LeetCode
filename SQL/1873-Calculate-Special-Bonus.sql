/*
Table: Employees (employee_id int, name varchar(30), salary int)

Write an SQL query to calculate the bonus of each employee. 
The bonus of an employee is 100% of their salary if 
the ID of the employee is an odd number and the employee name does not start with the character 'M'.
The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.
*/
SELECT employee_id,
CASE
  WHEN employee_id % 2 = 1 AND name REGEXP '^[^M]' THEN salary
  ELSE 0
END AS 'bonus'
FROM Employees
ORDER BY employee_id;