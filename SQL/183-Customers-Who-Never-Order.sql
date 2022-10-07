/*
Table: Customers (id int, name varchar(255))
Table: Orders (id int, customerId int)

Write an SQL query to report all customers who never order anything.
Return the result table in any order.
*/
-- Solution #1
SELECT Customers.name AS Customers
FROM Customers
LEFT JOIN Orders
ON Customers.id = Orders.customerId
WHERE Orders.customerId IS NULL;

-- Solution #2
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId FROM Orders
);