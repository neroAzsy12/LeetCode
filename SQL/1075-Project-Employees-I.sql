/*
Table: Project (project_id int, employee_id int)
Table: Employee (employee_id int, name varchar(10), experience_years int)

Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.
Return the result table in any order.
*/
SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM Project p
INNER JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY project_id;