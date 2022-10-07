/*
Table: Orders (order_number int, customer_number int)

Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
The test cases are generated so that exactly one customer will have placed more orders than any other customer.
*/
-- Solution #1
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1;

-- Solution #2: Follow up question 
-- What if more than one customer has the largest number of orders, can you find all the customer_number in this case?
SELECT customer_number
FROM Orders
GROUP BY customer_number
HAVING COUNT(order_number) = (
  SELECT MAX(order_count)
  FROM (
    SELECT COUNT(order_number) AS order_count
    FROM Orders
    GROUP BY customer_number
  ) AS subtable
);