/*
Table: Employee (id int, name varchar(255), salary int, managerId int)

Write an SQL query to find the employees who earn more than their managers.
Return the result table in any order.
*/
-- Solution #1
SELECT E.name AS Employee
FROM Employee E
LEFT JOIN Employee AS M
ON E.managerID = M.id
WHERE E.salary > M.salary;

-- Solution #2
SELECT e.name AS Employee
FROM Employee AS E, Employee AS M
WHERE E.managerId = M.id AND E.salary > M.salary;