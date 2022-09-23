/*
Table: Employee (empId int, name varchar(255), supervisor int, salary int)
Table: Bonus (empId int, bonus int)

Write a query to report the name and bonus amount of each employee with a bonus less than 1000.
*/
SELECT Employee.name, Bonus.bonus
FROM Employee
LEFT JOIN Bonus ON Employee.empId = Bonus.empId
WHERE Bonus.bonus < 1000 OR Bonus.bonus IS NULL;

SELECT name, bonus
FROM Employee
LEFT JOIN Bonus USING(empId)
WHERE bonus < 1000 OR bonus IS NULL;